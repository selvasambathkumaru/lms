from django.shortcuts import render
from .models import EmpDetails, LeaveRequest
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import EmpDetailSerializer, LeaveRequestSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions, generics
# Create your views here.

gender = {'1':'male', '2':'female'}
designation = ['Engineer', 'Sr.Engineer', 'Module Lead', 'Technical Lead', 'Project Lead', 'Associate Manager', 'Project Manager']
leavetype = ['personal', 'sick', 'casual']
roles = {1:'admin',2: 'manager', 3:'employee'}

####### Decorators #######
@api_view(['GET', 'POST'])
####### Authentication #######
# @authentication_classes([BasicAuthentication])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
####### Authentication #######
def Emp_list(request, format = None):
    if request.method == 'GET':
        Product_data = EmpDetails.objects.all()
        serializer = EmpDetailSerializer(Product_data, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmpDetailSerializer(data = request.data)
        if serializer["eligible_leave"] > 5:
            print("you are exceedind the limit 5")
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                print(serializer.errors)

####### Decorators #######
@api_view(['GET', 'PUT', 'DELETE'])
####### Authentication #######
# @authentication_classes([BasicAuthentication])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
####### Authentication #######
def Emp_detail(request, id, format = None):
    try:
        Product_data = EmpDetails.objects.get(pk = id)
    except EmpDetails.DoesNotExist:
        return Response(satus =status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EmpDetailSerializer(Product_data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = EmpDetailSerializer(Product_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Product_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LeaveRequestView(APIView):
    authentication_classes = [authentication .TokenAuthentication]
    permissions_classes = [permissions . IsAuthenticated]
    def post(self, request):
        serializer = LeaveRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        Product_data = LeaveRequest.objects.all()
        serializer = LeaveRequestSerializer(Product_data, many = True)
        return Response(serializer.data)
    
class LeaveRequestByLeaveTypeView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer

    def get_queryset(self):
        leave_type = self.kwargs['leave_type']
        return LeaveRequest.objects.filter(leave_type=leave_type)

class LeaveRequestApproveView(generics.UpdateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer(queryset, many = True)

    def put(self, request, *args, **kwargs):
        leave_request = self.get_object()
        leave_request.approved = True
        leave_request.approved_by = request.user
        leave_request.save()
        return Response(status=status.HTTP_200_OK)
    
class LeaveRequestCancelView(generics.UpdateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer(queryset, many = True)

    def put(self, request, *args, **kwargs):
        leave_request = self.get_object()
        leave_request.cancelled = True
        leave_request.cancelled_by = request.user
        leave_request.cancel_reason = request.data.get('cancel_reason', '')
        leave_request.save()
        return Response(status=status.HTTP_200_OK)

class LeaveRequestByEmployeeView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer

    def get_queryset(self):
        employee_name = self.kwargs['employee_name']
        return LeaveRequest.objects.filter(employee_name=employee_name)