# Generated by Django 2.1.3 on 2018-11-05 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(blank=True, null=True)),
                ('time_out', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('is_admin', models.BooleanField(blank=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_clocked_in', models.BooleanField(blank=True, default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sss_number', models.CharField(max_length=40)),
                ('pagibig_number', models.CharField(max_length=40)),
                ('philhealth_number', models.CharField(max_length=40)),
                ('tin_number', models.CharField(max_length=40)),
                ('rate_per_hour', models.FloatField(max_length=20)),
                ('non_working_days', models.CharField(blank=True, max_length=70)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMS_REST_API.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('birthday', models.DateField(default=None)),
                ('gender', models.CharField(max_length=15)),
                ('height', models.IntegerField(default=0)),
                ('contact_number', models.CharField(max_length=20)),
                ('absences_count', models.IntegerField(blank=True, default=0)),
                ('presences_count', models.IntegerField(blank=True, default=0)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMS_REST_API.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_cutoff', models.IntegerField(blank=True, default=5)),
                ('second_cutoff', models.IntegerField(blank=True, default=20)),
                ('level_1_rate', models.FloatField(blank=True, default=100, max_length=20)),
                ('level_2_rate', models.FloatField(blank=True, default=200, max_length=20)),
                ('level_3_rate', models.FloatField(blank=True, default=250, max_length=20)),
                ('overtime_rate', models.FloatField(blank=True, default=1.25, max_length=20)),
                ('regular_holiday_rate', models.FloatField(blank=True, default=1.0, max_length=20)),
                ('special_holiday_rate', models.FloatField(blank=True, default=0.3, max_length=20)),
                ('pagibig_contrib_rate', models.FloatField(blank=True, default=0.02)),
                ('philhealth_contrib_rate', models.FloatField(blank=True, default=0.01375)),
                ('sss_contrib_rate', models.FloatField(blank=True, default=0.0363)),
                ('tax_contrib_rate', models.FloatField(blank=True, default=0.0333)),
                ('tax_income_candidate', models.FloatField(blank=True, default=20833)),
                ('pagibig_pay_day', models.IntegerField(blank=True, default=20)),
                ('philhealth_pay_day', models.IntegerField(blank=True, default=20)),
                ('sss_pay_day', models.IntegerField(blank=True, default=20)),
                ('tax_pay_day', models.IntegerField(blank=True, default=20)),
                ('is_operating', models.BooleanField(default=True)),
                ('fb_page_id', models.CharField(default='1104237039735655', max_length=50)),
                ('fb_user_token', models.CharField(default='EAAZAUX1v4ACUBAEBVObGa91JTBH4QIXStTCqiZBGD8lF20DTydG9RffOIQ9pAG47dOfIsCNbwMbPeLpNbso4K8dh4QVJyC4jG4KXddlCSgM9zE6ZCo9ZAfLXD4nmOZCNvWFNoEvZCvM3efGhZAraFuBZAZA630ZCzBdekzs68WTQ4NOAZDZD', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.FloatField(blank=True, default=0)),
                ('total_over_time', models.FloatField(blank=True, default=0)),
                ('days_present', models.IntegerField(blank=True, default=0)),
                ('days_absent', models.IntegerField(blank=True, default=0)),
                ('sss_contrib', models.FloatField(blank=True, default=0, max_length=20)),
                ('philhealth_contrib', models.FloatField(blank=True, default=0, max_length=20)),
                ('pagibig_contrib', models.FloatField(blank=True, default=0, max_length=20)),
                ('tax', models.FloatField(blank=True, default=0, max_length=20)),
                ('special_pay', models.FloatField(blank=True, default=0, max_length=20)),
                ('gross_pay', models.FloatField(blank=True, default=0, max_length=20)),
                ('net_pay', models.FloatField(blank=True, default=0, max_length=20)),
                ('period', models.CharField(blank=True, max_length=60, null=True)),
                ('is_released', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMS_REST_API.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='attendancelog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMS_REST_API.Employee'),
        ),
    ]
