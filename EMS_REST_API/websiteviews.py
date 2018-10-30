import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMS_REST_API_project.settings')
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()

from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import Employee, EmployeeConfig, EmployeeProfile,\
    AttendanceLog, SalaryReport, GlobalConfig
from datetime import datetime
from dateutil.parser import parse
import pytz
time_zone = pytz.timezone('Asia/Manila')
import requests
from requests.auth import HTTPBasicAuth


# website views
def get_employee_object(user):
    user_object = User.objects.get(username=user)
    employee_object = Employee.objects.get(user=user_object.pk)
    return employee_object


def get_employee_profile(user):
    profile = EmployeeProfile.objects.get(user=user)
    return profile


def get_employee_config(user):
    config = EmployeeConfig.objects.get(user=user)
    return config


def convert_id(idx, yr):
    return 'GCC' + str(idx) + '-' + str(yr)[2:]


def landing(request):
    return render(request, 'EMS_REST_API/landingpage.html')


def loginview(request):
    # authenticated user redirect
    if request.user.is_authenticated:
        return HttpResponseRedirect('/emswebext/index/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user=user)
            return HttpResponseRedirect('/emswebext/index/')
        else:
            context = {
                'error': 'Incorrect username or password'
            }
            return render(request, 'EMS_REST_API/login.html', context=context)
    elif request.COOKIES.get('sessionid'):
        return HttpResponseRedirect('/emswebext/index/')
    else:
        return render(request, 'EMS_REST_API/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/emswebext/login/')


@ login_required
def index(request):
    user_object = User.objects.get(username=request.user)
    try:
        employee_object = get_employee_object(request.user)
    except:
        logout(request)
        return HttpResponseRedirect('/emswebext/login/')
    gcc_id = convert_id(employee_object.id, str(employee_object.start_date)[:4])
    context = {
        'user_object': user_object,
        'employee_object': employee_object,
        'employee_profile': get_employee_profile(employee_object.pk),
        'employee_config': get_employee_config(employee_object.pk),
        'gcc_id': gcc_id,
    }
    return render(request, 'EMS_REST_API/index.html', context=context)


@ login_required
def attendance(request):
    user_object = get_employee_object(request.user)
    context = {'employee_object': user_object}

    self_attendance = AttendanceLog.objects.filter(user=user_object.pk)
    formatted_self_attendance = []
    for i in self_attendance:
        time_in = i.time_in.astimezone(time_zone)
        time_in = str(time_in.strftime("%B %d, %Y %I:%M:%S %p"))
        time_out = ' '
        if i.time_out is not None:
            time_out = i.time_out.astimezone(time_zone)
            time_out = str(time_out.strftime("%B %d, %Y %I:%M:%S %p"))
        log_object = {'time_in': time_in, 'time_out': time_out}
        formatted_self_attendance.append(log_object)

    all_attendance = AttendanceLog.objects.all()
    formatted_all_attendance = []

    for i in all_attendance:
        employee_object = Employee.objects.get(pk=i.user_id)
        time_in = i.time_in.astimezone(time_zone)
        time_in = str(time_in.strftime("%B %d, %Y %I:%M:%S %p"))
        time_out = ' '
        if i.time_out is not None:
            time_out = i.time_out.astimezone(time_zone)
            time_out = str(time_out.strftime("%B %d, %Y %I:%M:%S %p"))
        gcc_id = convert_id(employee_object.id, str(employee_object.start_date)[:4])
        emp_name = '%s, %s %s' % (employee_object.last_name, employee_object.middle_name, employee_object.first_name)
        log_object = {'time_in': time_in, 'time_out': time_out, 'name': emp_name, 'id': gcc_id}
        formatted_all_attendance.append(log_object)

    context['attendance_logs'] = formatted_self_attendance
    if user_object.is_admin:
        context['attendance_logs'] = formatted_all_attendance

    return render(request, 'EMS_REST_API/attendance.html', context=context)


@ login_required
def salary(request):
    employee_object = get_employee_object(request.user)
    context = {'employee_object': employee_object}

    salary_objects = SalaryReport.objects.filter(user=employee_object.pk)
    formatted_salary_logs = []
    for i in salary_objects:

        period = 'Current'
        status = 'Current'
        if i.is_released:
            start_date = i.period.split(' - ')[0]
            start_date = parse(start_date)
            start_date = start_date.strftime("%b %d, %Y")
            end_date = i.period.split(' - ')[1]
            end_date = parse(end_date)
            end_date = end_date.strftime("%b %d, %Y")
            period = "  %s - %s" % (start_date, end_date)
            status = 'Released'

        log = {
            'total_time': i.total_time,
            'total_ot': i.total_over_time,
            'days_present': i.days_present,
            'days_absent': i.days_absent,
            'special_pay': 'PHP ' + str(round(i.special_pay, 2)),
            'gross_pay': 'PHP ' + str(round(i.gross_pay,2)),
            'sss': 'PHP ' + str(round(i.sss_contrib, 2)),
            'philhealth': 'PHP ' + str(round(i.philhealth_contrib, 2)),
            'pagibig': 'PHP ' + str(round(i.pagibig_contrib, 2)),
            'tax': 'PHP ' + str(round(i.tax, 2)),
            'total_deductions':
                'PHP ' + str(round(sum([i.sss_contrib, i.philhealth_contrib, i.pagibig_contrib, i.tax]),2)),
            'net_pay': 'PHP ' + str(round(i.net_pay, 2)),
            'period': period,
            'status': status,
        }

        formatted_salary_logs.append(log)

    salary_objects_all = SalaryReport.objects.all()
    formatted_salary_logs_all = []

    for i in salary_objects_all:
        salary_employee_object = Employee.objects.get(pk=i.user_id)
        emp_name = '%s, %s %s' % (salary_employee_object.last_name,
                                  salary_employee_object.middle_name, salary_employee_object.first_name)
        gcc_id = convert_id(salary_employee_object.id, str(salary_employee_object.start_date)[:4])

        period = 'Current'
        status = 'Current'
        if i.is_released:
            start_date = i.period.split(' - ')[0]
            start_date = parse(start_date)
            start_date = start_date.strftime("%B %d, %Y")
            end_date = i.period.split(' - ')[1]
            end_date = parse(end_date)
            end_date = end_date.strftime("%B %d, %Y")
            period = "  %s - %s" % (start_date, end_date)
            status = 'Released'

        log = {
            'gcc_id': gcc_id,
            'emp_name': emp_name,
            'total_time': i.total_time,
            'total_ot': i.total_over_time,
            'days_present': i.days_present,
            'days_absent': i.days_absent,
            'special_pay': 'PHP ' + str(round(i.special_pay, 2)),
            'gross_pay': 'PHP ' + str(round(i.gross_pay,2)),
            'sss': 'PHP ' + str(round(i.sss_contrib, 2)),
            'philhealth': 'PHP ' + str(round(i.philhealth_contrib, 2)),
            'pagibig': 'PHP ' + str(round(i.pagibig_contrib, 2)),
            'tax': 'PHP ' + str(round(i.tax, 2)),
            'total_deductions':
                'PHP ' + str(round(sum([i.sss_contrib, i.philhealth_contrib, i.pagibig_contrib, i.tax]),2)),
            'net_pay': 'PHP ' + str(round(i.net_pay, 2)),
            'period': period,
            'status': status,
        }

        formatted_salary_logs_all.append(log)

    context['salary_logs'] = formatted_salary_logs
    if employee_object.is_admin:
        context['salary_logs'] = formatted_salary_logs_all

    return render(request, 'EMS_REST_API/salary.html', context=context)


@ login_required
def employee_list(request):
    employee_object = get_employee_object(request.user)
    employee_object_list = Employee.objects.exclude(id=employee_object.pk)
    for i in employee_object_list:
        user_object = User.objects.get(id=i.user_id)
        i.username = user_object.username
        i.profile = EmployeeProfile.objects.get(user=i.pk)
        i.gcc_id = convert_id(i.id, str(i.start_date)[:4])
        i.full_name = '%s, %s %s' % (i.last_name, i.middle_name, i.first_name)

    context = {
        'employee_object': employee_object,
        'employee_object_list': employee_object_list,
    }

    return render(request, 'EMS_REST_API/employeelist.html', context=context)


@ login_required
def employee_profile(request, username, update_response=None):
    session_user_object = get_employee_object(request.user)
    try:
        user_object = User.objects.get(username=username)
        employee_object = Employee.objects.get(user=user_object.pk)
        gcc_id = convert_id(employee_object.id, str(employee_object.start_date)[:4])
        profile = get_employee_profile(employee_object.pk)
        profile.birthday = profile.birthday.strftime("%Y-%m-%d")
        config = get_employee_config(employee_object.pk)
        global_config = GlobalConfig.objects.last()

        context = {
            'username': username,
            'error': False,
            'update_response': update_response,
            'gcc_id': gcc_id,
            'user_object': user_object,
            'session_user': session_user_object,
            'employee_object': employee_object,
            'employee_profile': profile,
            'employee_config': config,
            'global_config': global_config,
        }
    except User.DoesNotExist:
        context = {
            'error': True,
        }

    return render(request, 'EMS_REST_API/employeeprofile.html', context=context)


@ login_required()
def update_employee(request):
    session_user_object = get_employee_object(request.user)
    if request.method == 'POST':
        try:
            employee_object = Employee.objects.get(pk=request.POST['id'])
            employee_profile_object = EmployeeProfile.objects.get(user=request.POST['id'])
            employee_config = EmployeeConfig.objects.get(user=request.POST['id'])

            dayoff_list = request.POST.getlist('dayoff')
            day_off = 'sunday'

            for i in dayoff_list:
                day_off += ', ' + i

            birthyear = int(request.POST['birthday'][:4])
            if (int(datetime.now().strftime("%Y")) - birthyear) < 17:
                update_error = 'Invalid Age'
                return employee_profile(request, request.POST['username'], update_error)

            is_admin = False
            if request.POST['position'] == 'administrator':
                is_admin = True
            employee_object.first_name = request.POST['first_name']
            employee_object.middle_name = request.POST['middle_name']
            employee_object.last_name = request.POST['last_name']
            employee_object.is_admin = is_admin
            employee_object.position = request.POST['position']
            employee_object.is_active = False
            if request.POST['status'] == 'active':
                employee_object.is_active = True
            employee_profile_object.address = request.POST['address']
            employee_profile_object.birthday = request.POST['birthday']
            employee_profile_object.gender = request.POST['gender']
            employee_profile_object.contact_number = request.POST['contact_number']

            employee_config.sss_number = request.POST['sss_number']
            employee_config.philhealth_number = request.POST['philhealth_number']
            employee_config.pagibig_number = request.POST['pagibig_number']
            employee_config.tin_number = request.POST['tin_number']
            employee_config.rate_per_hour = request.POST['rate_per_hour']
            employee_config.non_working_days = day_off

            employee_object.save()
            employee_profile_object.save()
            employee_config.save()
            update_success = 'ok'
            return employee_profile(request, request.POST['username'], update_success)
        except:
            return render(request, 'EMS_REST_API/error_404_full.html', context={'session_user': session_user_object})
    return render(request, 'EMS_REST_API/error_404_full.html', context={'session_user': session_user_object})


@ login_required
def update_email(request):
    if request.method == 'POST':
        email = request.POST['email'] + '@gmail.com'
        context = {'response': 'your email was updated'}
        check_existence = User.objects.filter(email=email).exists()
        user_object = User.objects.get(username=request.user)
        if user_object.email == email:
            context = {'response': 'you did not change your email at all'}
        if check_existence:
            context = {'response': 'a user already uses that gmail account'}
        else:
            user_object.email = email
            user_object.save()

        return render(request, 'EMS_REST_API/update_email.html', context=context)
    return render(request, 'EMS_REST_API/update_email.html')


@ login_required
def update_photo(request):
    if request.method == 'POST':
        employee_object = get_employee_object(request.user)
        profile = get_employee_profile(employee_object.pk)

        if 'picture' in request.FILES:
            profile.profile_photo = request.FILES['picture']

        profile.save()

    return HttpResponseRedirect('/emswebext/index/')


@ login_required
def global_config(request,  update_response=None):
    employee_object = get_employee_object(request.user)
    context = {
        'employee_object': employee_object,
        'update_response': update_response,
    }
    config = GlobalConfig.objects.last()
    context['config'] = config
    return render(request, 'EMS_REST_API/globalconfig.html', context=context)


@ login_required
def update_global_config(request):
    session_user_object = get_employee_object(request.user)
    if request.method == 'POST':
        is_operating = True
        if request.POST['is_operating'] == 'no':
            is_operating = False

        fcutoff = 15
        scutoff = 30
        if request.POST['cutoff'] == "5":
            fcutoff = 5
            scutoff = 20
        elif request.POST['cutoff'] == "10":
            fcutoff = 10
            scutoff = 25

        sss_pay = fcutoff
        if request.POST['sss_pay'] == "second":
            sss_pay = scutoff

        philhealth_pay = fcutoff
        if request.POST['philhealth_pay'] == "second":
            philhealth_pay = scutoff

        pagibig_pay = fcutoff
        if request.POST['pagibig_pay'] == "second":
            pagibig_pay = scutoff

        tax_pay = fcutoff
        if request.POST['tax_pay'] == "second":
            tax_pay = scutoff

        if any(float(i) < 50 for i in [request.POST['level_1_rate'], request.POST['level_2_rate'],
                                request.POST['level_3_rate']]):
            note = 'any of rates should not be less than PHP 50'
            return global_config(request, update_response=note)

        if float(request.POST['level_1_rate']) >= float(request.POST['level_2_rate'])\
                or float(request.POST['level_1_rate']) >= float(request.POST['level_3_rate'])\
                or float(request.POST['level_2_rate']) >= float(request.POST['level_3_rate']):
            note = 'rates should vary. level 1 rate < level 2 rate < level 3 rate'
            return global_config(request, update_response=note)

        if float(request.POST['ot_rate']) < 1:
            note = 'overtime rate should not be less than 1'
            return global_config(request, update_response=note)

        content = {
            'first_cutoff': fcutoff,
            'level_1_rate': request.POST['level_1_rate'],
            'level_2_rate': request.POST['level_2_rate'],
            'level_3_rate': request.POST['level_3_rate'],
            'ot_rate': request.POST['ot_rate'],
            'sss_pay_day': sss_pay,
            'philhealth_pay_day': philhealth_pay,
            'pagibig_pay_day': pagibig_pay,
            'tax_pay_day': tax_pay,
            'is_operating': is_operating
        }

        # UPDATE THIS WHEN YOU UPLOAD AT HOST
        requests.post('http://localhost:8000/updateGlobalConfig/', data=content,
                      auth=HTTPBasicAuth(username='cedrick', password='longview048'))

        update_success = 'ok'
        return global_config(request, update_response=update_success)
    return render(request, 'EMS_REST_API/error_404_full.html', context={'session_user': session_user_object})
