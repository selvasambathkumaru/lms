from django.urls import path
from . import views
from .views import LeaveRequestView, LeaveRequestListView, LeaveRequestViewSet
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'lmsdetails'


urlpatterns = [
    # path('create_role/', views.create_role),    
    path('employees/', views.Emp_list),
    path('employees/<int:id>', views.Emp_detail),
    path('employee/login/', obtain_auth_token),
    path('leave-request/', LeaveRequestView.as_view()),
    # # path('leave-request/<str:employee_name>/', LeaveRequestByEmployeeView.as_view()),
    # path('leave-request/<str:leave_type>/', LeaveRequestByLeaveTypeView.as_view()),
    path('leave-request/list/', LeaveRequestListView.as_view(), name='leave-request-list'),
    path('leave-request/approve/<int:pk>/', LeaveRequestViewSet.as_view({'get': 'approve'})),
    path('leave-request/cancel/<int:pk>/', LeaveRequestViewSet.as_view({'get': 'cancel'})),
    path('leave-request/permission/', LeaveRequestViewSet.as_view({'get': 'get_permissions'})),
]