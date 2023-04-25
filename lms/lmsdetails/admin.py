from django.contrib import admin
from .models import EmpDetails, LeaveRequest
# Register your models here.

admin.site.register(EmpDetails)

admin.site.register(LeaveRequest)