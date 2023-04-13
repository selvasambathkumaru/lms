from django.urls import path
from . import views
from .views import LeaveRequestView, LeaveRequestByLeaveTypeView, LeaveRequestApproveView, LeaveRequestCancelView, LeaveRequestByEmployeeView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'lmsdetails'


urlpatterns = [
    
    path('employees/', views.Emp_list),
    path('employees/<int:id>', views.Emp_detail),
    path('employee/login/', obtain_auth_token),
    path('leave-request/', LeaveRequestView.as_view()),
    path('leave-request/<str:leave_type>/', LeaveRequestByLeaveTypeView.as_view()),
    path('leave-request/approve/<int:pk>/', LeaveRequestApproveView.as_view(), name='leave_request_approve'),
    path('leave-request/cancel/<int:pk>/', LeaveRequestCancelView.as_view(), name='leave_request_cancel'),
    path('leave-request/<str:employee_name>/', LeaveRequestByEmployeeView.as_view(), name='leave_request_by_employee'),

]