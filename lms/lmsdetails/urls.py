from django.urls import path
from . import views
from .views import LeaveRequestView, LeaveRequestFilterView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'lmsdetails'


urlpatterns = [
    
    path('employees/', views.Emp_list),
    path('employees/<int:id>', views.Emp_detail),
    path('employee/login/', obtain_auth_token),
    path('leave-request/', LeaveRequestView.as_view()),
    path('leave-request/filter/', LeaveRequestFilterView.as_view()),

]