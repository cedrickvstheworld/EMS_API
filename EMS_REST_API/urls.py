from django.urls import path, include
from rest_framework import routers
from . import views
from . import websiteviews

router = routers.DefaultRouter()
router.register('User', views.UserView, 'User')
router.register('Employee', views.EmployeeView, 'Employee')
router.register('EmployeeConfig', views.EmployeeConfigView, 'EmployeeConfig')
router.register('EmployeeProfile', views.EmployeeProfileView, 'EmployeeProfile')
router.register('AttendanceLog', views.AttendanceLogView, 'AttendanceLog')
router.register('SalaryReport', views.SalaryReportView, 'SalaryReport')
router.register('GlobalConfig', views.GlobalConfigView, 'GlobalConfig')
urlpatterns = [
    # API_VIEWS
    path('', include(router.urls)),
    path('registerEmployee/', views.RegisterUser.as_view(), name='registerEmployee'),
    path('adminVerify/', views.AdminVerify.as_view(), name='adminVerify'),
    path('recordAttendance/', views.RecordAttendance.as_view(), name='recordAttendance'),
    path('userInfo/', views.GetUserInfo.as_view(), name='userInfo'),
    path('updateGlobalConfig/', views.UpdateGlobalConfig.as_view(), name='updateGlobalConfig'),
    path('updateEmployee/', views.UpdateEmployee.as_view(), name='updateEmployee'),
    path('updateStatus/', views.UpdateStatus.as_view(), name='updateStatus'),

    # WEBSITE_VIEWS
    path('emswebext/', websiteviews.landing, name='emswebext'),
    path('emswebext/login/', websiteviews.loginview, name='login_url'),
    path('emswebext/logout/', websiteviews.user_logout, name='logout_url'),
    path('emswebext/index/', websiteviews.index, name='index'),
    path('emswebext/attendance/', websiteviews.attendance, name='attendance'),
    path('emswebext/salary/', websiteviews.salary, name='salary'),
    path('emswebext/employeelist/', websiteviews.employee_list, name='employeelist'),
    path('emswebext/employeeprofile/<username>/', websiteviews.employee_profile, name='employeeprofile'),
    path('emswebext/employeeUpdate/', websiteviews.update_employee, name='employeeUpdateWebsite'),
    path('emswebext/globalConfig/', websiteviews.global_config, name='globalConfig'),
    path('emswebext/configUpdate/', websiteviews.update_global_config, name='configUpdateWebsite'),
    path('emswebext/updateEmail/', websiteviews.update_email, name='updateemail'),
    path('emswebext/updatePhoto/', websiteviews.update_photo, name='updatephoto'),
]




