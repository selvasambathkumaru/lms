from django.urls import path
from . import views
from .views import LeaveRequestView, LeaveRequestListView, LeaveRequestViewSet, UserListCreateView,UserRetrieveUpdateDestroyView, AdminListCreateView, EmployeeListCreateView, AdminView, EmployeeView

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'lmsdetails'


urlpatterns = [
    path('employee/login/', obtain_auth_token),   
    path('employees/', views.Emp_list),
    path('employees/<int:id>', views.Emp_detail),
    path('leave-request/', LeaveRequestView.as_view()),
    path('leave-request/<int:id>', views.LeaveRequestbyId),
    path('emp_users/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('emp_users/<int:pk>/', EmployeeView.as_view(), name='user-retrieve-update-destroy'),
    path('admin_users/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admin_users/<int:pk>/', AdminView.as_view(), name='user-retrieve-update-destroy'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    # # path('leave-request/<str:employee_name>/', LeaveRequestByEmployeeView.as_view()),
    # path('leave-request/<str:leave_type>/', LeaveRequestByLeaveTypeView.as_view()),
    path('leave-request/list/', LeaveRequestListView.as_view(), name='leave-request-list'),
    path('leave-request/approve/<int:pk>/', LeaveRequestViewSet.as_view({'get': 'approve'})),
    path('leave-request/cancel/<int:pk>/', LeaveRequestViewSet.as_view({'get': 'cancel'})),
]