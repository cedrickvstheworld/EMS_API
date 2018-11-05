from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from . models import Employee, EmployeeConfig, EmployeeProfile,\
    AttendanceLog, SalaryReport, GlobalConfig
from . serializers import UserSerializer, EmployeeSerializer, EmployeeConfigSerializer, EmployeeProfileSerializer,\
      AttendanceLogSerializer, SalaryReportSerializer, GlobalConfigSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts
from datetime import date, datetime, timedelta
from pytz import timezone
import pytz
from dateutil.parser import parse
import calendar
from . timeprocess import DateProcess, TimeCompute
from . payprocess import PayProcess
import schedule
import time
import threading
from dateutil.parser import parse
import pytz

# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = User.objects.all()


class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = Employee.objects.all()


class EmployeeConfigView(viewsets.ModelViewSet):
    serializer_class = EmployeeConfigSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = EmployeeConfig.objects.all()


class EmployeeProfileView(viewsets.ModelViewSet):
    serializer_class = EmployeeProfileSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = EmployeeProfile.objects.all()


class AttendanceLogView(viewsets.ModelViewSet):
    serializer_class = AttendanceLogSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = AttendanceLog.objects.all()


class SalaryReportView(viewsets.ModelViewSet):
    serializer_class = SalaryReportSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = SalaryReport.objects.all().order_by('-id')


class GlobalConfigView(viewsets.ModelViewSet):
    serializer_class = GlobalConfigSerializer
    permission_classes = (permissions.IsAuthenticated and permissions.IsAdminUser,)
    queryset = GlobalConfig.objects.all().order_by('-id')


# special functions
def is_active_validation(user_id):
    try:
        employee_object = Employee.objects.get(id=user_id)
        if employee_object.is_active:
            return True
        return False
    except Employee.DoesNotExist:
        pass


def get_employee_object(user_id, user_password):
    try:
        user_object = User.objects.get(id=user_id)
        try:
            authCheck = authenticate(username=user_object.username, password=user_password)
            if authCheck:
                employee_object = Employee.objects.get(user=user_object)
                return employee_object
            return 'Incorrect Password'
        except Employee.DoesNotExist:
            return 'Hi Creator'
    except User.DoesNotExist:
        return 'you are not registered'


def get_weekday(cur_datetime):
    format_str = '%Y-%m-%d'
    datetime_obj = datetime.strptime(cur_datetime.split(' ')[0], format_str)
    weekday = calendar.day_name[datetime_obj.date().weekday()].lower()
    return weekday


def get_datetimePH():
    t =  datetime.now(timezone('Asia/Manila')).strftime('%Y-%m-%d %H:%M:%S')
    return t


def auto_clock_out():
    print('auto clock-out check . . .')
    attendance_objects = AttendanceLog.objects.filter(time_out=None)
    for i in attendance_objects:
        employee_object = Employee.objects.get(id=i.user_id)
        i.time_out = datetime.now(timezone('UTC'))
        i.save()
        employee_object.is_clocked_in = False
        employee_object.save()
        update_salary(i.time_out, i.time_in, employee_object)
    print('auto clock-out check done')


def update_salary(time_out, time_in, employee_object):
    time_diff = TimeCompute([time_out, time_in])
    total_time = time_diff.get_time_diff()
    employee_config_object = EmployeeConfig.objects.get(user=employee_object)
    employee_rate = employee_config_object.rate_per_hour
    special_pay = 0
    initial_gross_pay = employee_rate * total_time

    global_config = GlobalConfig.objects.last()
    special_holiday_multiplier = global_config.special_holiday_rate
    regular_holiday_multiplier = global_config.regular_holiday_rate

    holiday_check = DateProcess(datetime.now(timezone('Asia/Manila')))
    if holiday_check.holiday_check() == 'regular':
        special_pay = initial_gross_pay * regular_holiday_multiplier
    elif holiday_check.holiday_check() == 'special':
        special_pay = initial_gross_pay * special_holiday_multiplier

    gross_pay = initial_gross_pay + special_pay

    check_existence = SalaryReport.objects.filter(user=employee_object).exists()

    if check_existence:
        last_log = SalaryReport.objects.filter(user=employee_object).last()

        if last_log.is_released:
            SalaryReport.objects.get_or_create(
                user=employee_object,
                gross_pay=gross_pay,
                special_pay=special_pay,
                total_time=total_time,
            )

        else:
            last_log.gross_pay += gross_pay
            last_log.special_pay += special_pay
            last_log.total_time += total_time
            last_log.save()

    else:
        SalaryReport.objects.get_or_create(
            user=employee_object,
            gross_pay=gross_pay,
            special_pay=special_pay,
            total_time=total_time,
        )


def release_salary(date_time):
    print('salary release check ...')
    salary_objects = SalaryReport.objects.filter(is_released=False)
    global_config_object = GlobalConfig.objects.last()

    first_cut_off = global_config_object.first_cutoff
    second_cut_off = global_config_object.second_cutoff

    day_of_month = int(date_time.strftime('%d'))
    month = int(date_time.strftime('%m'))

    if month == 2 and second_cut_off >= 28:
        second_cut_off = 28

    if day_of_month == first_cut_off or day_of_month == second_cut_off:
        date_process_object = DateProcess(datetime.now(timezone('Asia/Manila')))
        period = date_process_object.get_pay_period()
        for i in salary_objects:
            second_last_income = 0

            i_objects = SalaryReport.objects.filter(Q(user=i.user) & Q(is_released=True)).last()
            try:
                second_last_income = i_objects.gross_pay
            except:
                pass

            income_con = PayProcess((i.gross_pay + second_last_income), day_of_month)

            i.sss_contrib = income_con.sss_contrib()
            i.tax = income_con.tax_contrib()
            i.philhealth_contrib = income_con.philhealth_contrib()
            i.pagibig_contrib = income_con.pagibig_contrib()
            i.net_pay = i.gross_pay - income_con.get_contributions()
            i.period = period
            i.is_released = True
            i.save()
    print('salary release check done')


def overtime_check():
    print('overtime check ...')
    time_zone = pytz.timezone('Asia/Manila')
    global_config_object = GlobalConfig.objects.last()
    employee_objects = Employee.objects.exclude(is_active=False)

    date_today = datetime.now(timezone('Asia/Manila'))
    for i in employee_objects:
        attendance_logs_today = AttendanceLog.objects.filter(user=i.pk)
        logs_time_diff = []
        for logs in attendance_logs_today:
            time_in_parsed = logs.time_in.astimezone(time_zone)
            time_in_parsed = time_in_parsed.strftime("%Y-%m-%d")
            if time_in_parsed != date_today.strftime("%Y-%m-%d"):
                continue

            timeOut = logs.time_out
            if logs.time_out is None:
                timeOut = datetime.now(timezone('UTC'))
            time_diff = TimeCompute([timeOut, logs.time_in])
            total_time = time_diff.get_time_diff()
            logs_time_diff.append(total_time)

        total_time = sum(logs_time_diff)

        overtime = 0
        if total_time > 8:
            overtime = total_time - 8

        try:
            employee_salary = SalaryReport.objects.get(Q(user=i.pk) & Q(is_released=False))
        except SalaryReport.DoesNotExist:
            continue
        employee_config = EmployeeConfig.objects.get(user=i.pk)

        employee_salary.total_over_time += overtime

        rate = employee_config.rate_per_hour
        ot_rate = global_config_object.overtime_rate

        ot_pay = round(((overtime * rate * ot_rate) - (overtime * rate)), 2)


        employee_salary.gross_pay += ot_pay

        employee_salary.save()

    print('overtime check done')




def check_attendance_status():
    print('attendance status check ...')
    time_zone = pytz.timezone('Asia/Manila')
    current_weekday = get_weekday(get_datetimePH())
    employee_objects = Employee.objects.exclude(Q(employeeconfig__non_working_days__icontains=current_weekday)
                                                | Q(is_active=False))
    for i in employee_objects:
        employee_profile = EmployeeProfile.objects.get(user=i)
        check_log_existence = AttendanceLog.objects.filter(user=i).exists()
        salary_log_existence = SalaryReport.objects.filter(Q(user=i) & Q(is_released=False)).exists()
        if salary_log_existence:
            salary_log = SalaryReport.objects.get(Q(user=i) & Q(is_released=False))
            if check_log_existence:
                attendance_log = AttendanceLog.objects.filter(user=i).last()

                last_log_in = attendance_log.time_in.astimezone(time_zone)
                last_log_in = last_log_in.strftime("%Y-%m-%d")
                current_date = datetime.now(timezone('Asia/Manila')).strftime('%Y-%m-%d')

                if last_log_in != current_date:
                    employee_profile.absences_count += 1
                    employee_profile.save()
                    salary_log.days_absent += 1
                    salary_log.save()
                else:
                    employee_profile.presences_count += 1
                    employee_profile.save()
                    salary_log.days_present += 1
                    salary_log.save()
            else:
                employee_profile.absences_count += 1
                employee_profile.save()
                salary_log.days_absent += 1
                salary_log.save()
        else:
            log_create = SalaryReport.objects.create(user=i)
            log_create.days_absent = 1
            log_create.save()
            employee_profile.absences_count = 1
            employee_profile.save()
    print('attendance status check done')


def periodical_run():
    try:
        config_object = GlobalConfig.objects.last()
        if config_object.is_operating:
            schedule.every().day.at("15:59").do(auto_clock_out)
            schedule.every().day.at("15:59").do(overtime_check)
            schedule.every().day.at("15:59").do(check_attendance_status)
            schedule.every().day.at("15:59").do(lambda: release_salary(datetime.now()))
            while True:
                schedule.run_pending()
                time.sleep(1)
    except:
        print('no configs was set..')


def run_thread():
    t = threading.Thread(target=periodical_run)
    t.start()


# thread
run_thread()



# # # # # # API Views # # # # # #


# employee registration
class RegisterUser(APIView):
    def post(self, request):

        context = {'request': request}
        request.data._mutable = True

        user = UserSerializer(data=request.data, context=context)
        employee = EmployeeSerializer(data=request.data, context=context)
        employee_config = EmployeeConfigSerializer(data=request.data, context=context)
        employee_profile = EmployeeProfileSerializer(data=request.data, context=context)


        try:
            validate_password(request.data['password'], user=None, password_validators=None)
        except:
            pass_error = password_validators_help_texts()
            return Response(pass_error, status=status.HTTP_400_BAD_REQUEST)

        email_exists = User.objects.filter(email=request.data['email']).exists()

        if email_exists:
            email_error = ['a user already uses that gmail account']
            return Response(email_error, status=status.HTTP_400_BAD_REQUEST)

        if user.is_valid():
            x = user.save()
            x.set_password(x.password)
            x.save()
            user_object = User.objects.get(username=request.data['username'])
            user_id = user_object.pk
            request.data['user'] = user_object.pk
            if employee.is_valid():
                employee.save()
                employee_object = Employee.objects.get(user=request.data['user'])
                request.data['user'] = employee_object.pk
                if employee_config.is_valid() and employee_profile.is_valid():
                    employee_config.save()
                    employee_profile.save()
                    return Response([True, user_id], status=status.HTTP_201_CREATED)
        user_error = []
        try:
            username_error = user.errors['username'][0]
            user_error.append(username_error)
        except:
            pass
        try:
            email_error = user.errors['email'][0]
            user_error.append(email_error)
        except:
            pass
        return Response(user_error, status=status.HTTP_400_BAD_REQUEST)


# master verification
# class MasterVerify(APIView):
#     def get(self, request):
#         authCheck = authenticate(username='cedrick', password=request.data['password'])
#         if authCheck:
#             return Response(True, status=status.HTTP_200_OK)
#         return Response(False, status=status.HTTP_200_OK)


# admin verification
class AdminVerify(APIView):
    def get(self, request):
        employee_object = get_employee_object(request.data['user'], request.data['password'])

        try:
            if employee_object.is_admin and employee_object.is_active:
                return Response(True, status=status.HTTP_200_OK)
            return Response(False, status=status.HTTP_200_OK)
        except:
            return Response(employee_object, status=status.HTTP_200_OK)


class RecordAttendance(APIView):
    def post(self, request):
        context = {'request': request}
        employee_object = get_employee_object(request.data['user_id'], request.data['password'])
        employee_id = employee_object.pk
        active_validity = is_active_validation(employee_id)
        if active_validity is False:
            return Response([employee_id, 'You are not authorized for this action anymore'], status=status.HTTP_200_OK)

        employee_config_object = EmployeeConfig.objects.get(user=employee_id)

        non_working_day = employee_config_object.non_working_days

        global_config_object = GlobalConfig.objects.last()

        current_weekday = get_weekday(get_datetimePH())


        current_datetime = datetime.now(timezone('UTC'))
        time_zone_ph = timezone('Asia/Manila')
        current_datetime_ph = datetime.now(time_zone_ph)

        end_time = current_datetime_ph.replace(hour=20, minute=0, second=0, microsecond=0)
        start_time = current_datetime_ph.replace(hour=5, minute=0, second=0, microsecond=0)

        if (request.data['command'] == 'clock-in' and
            (start_time > current_datetime_ph or current_datetime_ph > end_time))\
                or global_config_object.is_operating is False:
            response = 'you cannot log-in at this time'
            return Response([employee_id, response], status=status.HTTP_200_OK)

        clockIn = {
            'user': employee_id,
            'time_in': current_datetime,
        }

        clockOut = {
            'user': employee_id,
            'time_out': current_datetime,
        }

        attendance = AttendanceLogSerializer(data=clockIn, context=context)

        if request.data['command'] == 'clock-out':
            attendance = AttendanceLogSerializer(data=clockOut, context=context)

        if current_weekday in non_working_day:
            return Response([employee_id, 'today was scheduled as your non-working day'], status=status.HTTP_200_OK)


        check_existence = AttendanceLog.objects.filter(user=employee_id).exists()
        if check_existence:
            fetch_log = AttendanceLog.objects.filter(user=employee_id).last()

            response = None
            # case1 = time_in is not Null
            if fetch_log.time_in is not None and request.data['command'] == 'clock-in' and fetch_log.time_out is None:
                response = 'you are currently clocked in'

            # case2 = time_out is not Null
            elif fetch_log.time_out is not None and request.data['command'] == 'clock-out':
                response = 'you are not clocked in'

            # case3 = going to clock in:
            elif request.data['command'] == 'clock-in':
                if attendance.is_valid():
                    attendance.save()
                    employee_object.is_clocked_in = True
                    employee_object.save()
                    response = 'clocked-in'

            # case3 = going to clock out:
            elif request.data['command'] == 'clock-out':
                if current_datetime < fetch_log.time_in:
                    response = 'you could not sign-out, please check if the time is properly set'
                else:
                    fetch_log.time_out = current_datetime
                    fetch_log.save()
                    employee_object.is_clocked_in = False
                    employee_object.save()
                    response = 'clocked-out'
                    update_salary(fetch_log.time_out, fetch_log.time_in, employee_object)
            return Response([employee_id, response], status=status.HTTP_200_OK)

        else:
            if request.data['command'] == 'clock-out':
                return Response([employee_id, 'you are not clocked in'], status=status.HTTP_200_OK)
            if attendance.is_valid():
                attendance.save()
                employee_object.is_clocked_in = True
                employee_object.save()
                return Response([employee_id, 'clocked-in'], status=status.HTTP_200_OK)
            return Response(attendance.errors, status=status.HTTP_200_OK)


# update Global Config client-Admin Level
class UpdateGlobalConfig(APIView):
    def post(self, request):
        context = {'request': request}

        old_config = GlobalConfig.objects.last()
        old_lvl1_rate = old_config.level_1_rate
        old_lvl2_rate = old_config.level_2_rate
        old_lvl3_rate = old_config.level_3_rate

        global_conf = GlobalConfigSerializer(data=request.data, context=context)
        if global_conf.is_valid():
            global_conf.save()

            employee_configs = EmployeeConfig.objects.all()

            for i in employee_configs:
                if i.rate_per_hour == old_lvl1_rate:
                    i.rate_per_hour = request.data['level_1_rate']
                elif i.rate_per_hour == old_lvl2_rate:
                    i.rate_per_hour = request.data['level_2_rate']
                elif i.rate_per_hour == old_lvl3_rate:
                    i.rate_per_hour = request.data['level_3_rate']
                i.save()
            return Response('configurations are updated', status.HTTP_200_OK)
        return Response(global_conf.errors, status.HTTP_200_OK)


class UpdateEmployee(APIView):
    def post(self, request):
        employee_object = Employee.objects.get(pk=request.data['id'])
        employee_profile = EmployeeProfile.objects.get(user=request.data['id'])
        employee_config = EmployeeConfig.objects.get(user=request.data['id'])

        try:
            employee_object.first_name = request.data['first_name']
            employee_object.middle_name = request.data['middle_name']
            employee_object.last_name = request.data['last_name']
            employee_object.is_admin = request.data['is_admin']
            employee_object.position = request.data['position']
            employee_object.is_active = request.data['is_active']
            employee_profile.address = request.data['address']
            employee_profile.birthday = request.data['birthday']
            employee_profile.gender = request.data['gender']
            employee_profile.height = request.data['height']
            employee_profile.contact_number = request.data['contact_number']

            employee_config.sss_number = request.data['sss_number']
            employee_config.philhealth_number = request.data['philhealth_number']
            employee_config.pagibig_number = request.data['pagibig_number']
            employee_config.tin_number = request.data['tin_number']
            employee_config.rate_per_hour = request.data['rate_per_hour']
            employee_config.non_working_days = request.data['non_working_days']

            employee_object.save()
            employee_profile.save()
            employee_config.save()

            return Response('nice mother fucker', status.HTTP_200_OK)

        except:
            return Response('something is wrong', status.HTTP_400_BAD_REQUEST)

class GetUserInfo(APIView):
    def get(self, request):
        get_userInfo = User.objects.get(id=request.data['emp_id'])
        return Response([get_userInfo.username, get_userInfo.email, get_userInfo.id])


class UpdateStatus(APIView):
    def post(self, request):
        employee_object = Employee.objects.get(pk=request.data['id'])
        if employee_object.is_active is True:
            employee_object.is_active = False
        else:
            employee_object.is_active = True
        employee_object.save()
        return Response('Employee\'s status was updated', status=status.HTTP_200_OK)
