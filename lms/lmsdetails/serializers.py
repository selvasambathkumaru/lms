from rest_framework import serializers
from . models import EmpDetails, LeaveRequest, User

# class RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'is_employee']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_manager']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'is_manager']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'is_admin']


class EmpDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpDetails
        fields = '__all__'

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
