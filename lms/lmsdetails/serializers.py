from rest_framework import serializers
from . models import EmpDetails, LeaveRequest

# class RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = '__all__'

class EmpDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpDetails
        fields = '__all__'

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
