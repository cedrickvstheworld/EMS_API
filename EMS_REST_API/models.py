from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    is_admin = models.BooleanField(blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True, blank=True)
    is_clocked_in = models.BooleanField(default=False, blank=True)


class EmployeeConfig(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sss_number = models.CharField(max_length=40)
    pagibig_number = models.CharField(max_length=40)
    philhealth_number = models.CharField(max_length=40)
    tin_number = models.CharField(max_length=40)
    rate_per_hour = models.FloatField(max_length=20)
    non_working_days = models.CharField(max_length=70, blank=True)


class EmployeeProfile(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    birthday = models.DateField(default=None)
    gender = models.CharField(max_length=15)
    height = models.IntegerField(default=0)
    contact_number = models.CharField(max_length=20)
    absences_count = models.IntegerField(default=0, blank=True)
    presences_count = models.IntegerField(default=0, blank=True)
    profile_photo = models.ImageField(blank=True, null=True)


class AttendanceLog(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_in = models.DateTimeField(blank=True, null=True)
    time_out = models.DateTimeField(blank=True, null=True)


class SalaryReport(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_time = models.FloatField(default=0, blank=True)
    total_over_time = models.FloatField(default=0, blank=True)
    days_present = models.IntegerField(default=0, blank=True)
    days_absent = models.IntegerField(default=0, blank=True)
    sss_contrib = models.FloatField(max_length=20, default=0, blank=True)
    philhealth_contrib = models.FloatField(max_length=20, default=0, blank=True)
    pagibig_contrib = models.FloatField(max_length=20, default=0, blank=True)
    tax = models.FloatField(max_length=20, default=0, blank=True)
    special_pay = models.FloatField(max_length=20, default=0, blank=True)
    gross_pay = models.FloatField(max_length=20, default=0, blank=True)
    net_pay = models.FloatField(max_length=20, default=0, blank=True)
    period = models.CharField(max_length=60, blank=True, null=True)
    is_released = models.BooleanField(default=False, blank=True)


class GlobalConfig(models.Model):
    first_cutoff = models.IntegerField(default=5, blank=True)
    second_cutoff = models.IntegerField(default=20, blank=True)

    level_1_rate = models.FloatField(max_length=20, default=100, blank=True)
    level_2_rate = models.FloatField(max_length=20, default=200, blank=True)
    level_3_rate = models.FloatField(max_length=20, default=250, blank=True)
    overtime_rate = models.FloatField(max_length=20, default=1.25, blank=True)

    regular_holiday_rate = models.FloatField(max_length=20, default=1.0, blank=True)
    special_holiday_rate = models.FloatField(max_length=20, default=.30, blank=True)

    pagibig_contrib_rate = models.FloatField(default=0.02, blank=True)
    philhealth_contrib_rate = models.FloatField(default=0.01375, blank=True)
    sss_contrib_rate = models.FloatField(default=0.0363, blank=True)
    tax_contrib_rate = models.FloatField(default=0.0333, blank=True)

    tax_income_candidate = models.FloatField(default=20833, blank=True)

    pagibig_pay_day = models.IntegerField(default=20, blank=True)
    philhealth_pay_day = models.IntegerField(default=20, blank=True)
    sss_pay_day = models.IntegerField(default=20, blank=True)
    tax_pay_day = models.IntegerField(default=20, blank=True)

    is_operating = models.BooleanField(default=True)

    fb_page_id = models.CharField(max_length=50, default="1104237039735655")
    fb_user_token = models.CharField(max_length=255,
                                     default="EAAZAUX1v4ACUBAEBVObGa91JTBH4QIXStTCqiZBGD8lF20DTydG9RffOIQ9pAG47dOfIsCN"
                                             "bwMbPeLpNbso4K8dh4QVJyC4jG4KXddlCSgM9zE6ZCo9ZAfLXD4nmOZCNvWFNoEvZCvM3efGh"
                                             "ZAraFuBZAZA630ZCzBdekzs68WTQ4NOAZDZD")
