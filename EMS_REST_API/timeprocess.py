from datetime import datetime
from pytz import timezone
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMS_REST_API_project.settings')
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
from EMS_REST_API.models import GlobalConfig, AttendanceLog
# from EMS_REST_API.models import AttendanceLog

# refactored

class TimeCompute:
    def __init__(self, timelist):
        self.timelist = timelist

    def get_time_diff(self):
        timediff = self.timelist[0] - self.timelist[1]
        timediff_float = round((timediff.total_seconds() / 3600), 2)
        return timediff_float



# initial_code_pattern . . . . .

# class TimeFuck:
#     def __init__(self, timelist):
#         self.timelist = timelist
#
#     def convert_time_to_float(self, h, m, s):
#         float_time = (((m * 60) + s) / 3600) + h
#         return round(float_time, 2)
#
#     def segment_time(self, itime):
#         h = int(itime[0:2])
#         m = int(itime[3:5])
#         s = int(itime[6:8])
#
#         return h, m, s
#
#     def add_time(self):
#         time_set = []
#
#         for i in self.timelist:
#             h = self.segment_time(i)[0]
#             m = self.segment_time(i)[1]
#             s = self.segment_time(i)[2]
#             time_float = self.convert_time_to_float(h, m, s)
#             time_set.append(time_float)
#
#         time_sum = sum(time_set)
#
#         return round(time_sum, 2)
#
#     def subtract_time(self):
#         hMinuend = self.segment_time(self.timelist[0])[0]
#         hSubtrahend = self.segment_time(self.timelist[1])[0]
#
#         mMinuend = self.segment_time(self.timelist[0])[1]
#         mSubtrahend = self.segment_time(self.timelist[1])[1]
#
#         sMinuend = self.segment_time(self.timelist[0])[2]
#         sSubtrahend = self.segment_time(self.timelist[1])[2]
#
#         minuend = self.convert_time_to_float(hMinuend, mMinuend, sMinuend)
#         subtrahend = self.convert_time_to_float(hSubtrahend, mSubtrahend, sSubtrahend)
#
#         time_diff = minuend - subtrahend
#
#         if time_diff < 0:
#             time_diff = time_diff + 24
#
#         return round(time_diff, 2)


class DateProcess:
    def __init__(self, datex):
        self.date_partition = datex.strftime('%m-%d')
        self.regular_holiday_list = ['01-01', '03-29', '03-30', '04-09', '05-01', '06-12',
                                     '06-15', '07-21', '07-27', '11-30', '12-25', '12-30']
        self.special_holiday_list = ['01-02', '02-16', '02-25', '03-31',
                                     '08-21', '11-02', '12-24']

        # source: https://kittelsoncarpo.com/labor-employment/national-official-nonworking-holidays/

        self.end_date = datex.strftime('%Y-%m-%d')
        self.end_year = datex.strftime('%Y')
        self.end_month = datex.strftime('%m')
        self.end_day = datex.strftime('%d')

        self.global_config_object = GlobalConfig.objects.last()
        self.first_cut_off = self.global_config_object.first_cutoff
        self.second_cut_off = self.global_config_object.second_cutoff

    def holiday_check(self):
        if self.date_partition in self.regular_holiday_list:
            return 'regular'
        elif self.date_partition in self.special_holiday_list:
            return 'special'
        else:
            return False

    def leap_year_check(self):
        cur_year = int(self.end_year)
        if cur_year % 4 != 0:
            return False
        elif cur_year % 100 != 0:
            return True
        elif cur_year % 400 != 0:
            return False
        else:
            return True

    def get_pay_period(self):
        start_month = self.end_month
        start_day = str(self.first_cut_off + 1)
        start_year = self.end_year
        if int(self.end_day) == self.first_cut_off:
            if self.end_month == '1':
                start_month = '12'
                start_year = str(int(self.end_year) - 1)
            else:
                if self.end_day == '15':
                    start_day = '1'
                    start_month = self.end_month
                elif self.leap_year_check() and self.end_month == '3' and self.second_cut_off >= 28:
                    start_day = '1'
                else:
                    start_day = str(self.second_cut_off + 1)
                    start_month = str(int(self.end_month) - 1)
                start_year = self.end_year
        return "%s/%s/%s - %s/%s/%s" % (start_year, start_month, start_day,
                                        self.end_year, self.end_month, self.end_day)





# these fucking random characters are property of Cedrick
# x = Holiday(datetime(2018, 1, 2, 12, 32, 23, 0))
#
# print(x.check_day())

# x = TimeCompute([datetime(2018, 1, 2, 13, 52, 14, 0), datetime(2018, 1, 2, 10, 6, 36, 0)])
#
# print(x.get_time_diff())

# timetime = AttendanceLog.objects.last()
# print(timetime.time_in)
# x = DateProcess(timetime.time)
#
# print(x.get_pay_period())
