from django.shortcuts import render
from .models import EmpDetails, LeaveRequest, User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import EmpDetailSerializer, LeaveRequestSerializer, UserSerializer, EmployeeSerializer, AdminSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
# from django.contrib.auth.models import User
from rest_framework import authentication, permissions, generics
from rest_framework import viewsets
from django.db.models import Count

 
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        print (request.user)
        return request.user.is_authenticated and request.user.is_admin
    
class AdminListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]

class AdminView(generics.RetrieveUpdateAPIView):
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_object(self):
        return self.request.user
    
# Create your views here.
####### Decorators #######
@api_view(['GET', 'POST'])
####### Authentication #######
# @authentication_classes([BasicAuthentication])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdmin])
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
@permission_classes([IsAuthenticated, IsAdmin])
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

  
class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        print (request.user)
        return request.user.is_authenticated and request.user.is_employee

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployeeView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LeaveRequestView(APIView):
    authentication_classes = [authentication .TokenAuthentication]
    permissions_classes = [permissions . IsAuthenticated, IsEmployee]
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

####### Decorators #######
@api_view(['GET', 'PUT', 'DELETE'])
####### Authentication #######
# @authentication_classes([BasicAuthentication])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsEmployee])
####### Authentication #######
def LeaveRequestbyId(request, id, format = None):
    try:
        Product_data = LeaveRequest.objects.get(pk = id)
    except LeaveRequest.DoesNotExist:
        return Response(satus =status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LeaveRequestSerializer(Product_data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = LeaveRequestSerializer(Product_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Product_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class LeaveRequestByLeaveTypeView(generics.ListAPIView):
#     serializer_class = LeaveRequestSerializer

#     def get_queryset(self):
#         leave_type = self.kwargs['leave_type']
#         return LeaveRequest.objects.filter(leave_type=leave_type)

# class LeaveRequestByEmployeeView(generics.ListAPIView):
#     serializer_class = LeaveRequestSerializer

#     def get_queryset(self):
#         employee_name = self.kwargs['employee_name']
#         return LeaveRequest.objects.filter(employee_name=employee_name)

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        print (request.user)
        return request.user.is_authenticated and request.user.is_manager
        # return request.user.is_authenticated and (request.user.is_manager or request.user.is_superuser)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class LeaveRequestListView(generics.ListAPIView):
    """
    Full Leave Request List http://127.0.0.1:8000/leave-request/list/ and also
    Filtering list with employee name http://127.0.0.1:8000/leave-request/list/?employee_name=selva
    Filtering list with leave type http://127.0.0.1:8000/leave-request/list/?leave_type=sick
    """
    authentication_classes = [authentication .TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsManager]

    serializer_class = LeaveRequestSerializer

    def get_queryset(self):
        queryset = LeaveRequest.objects.all()
        employee_name = self.request.query_params.get('employee_name', None)
        leave_type = self.request.query_params.get('leave_type', None)
        if employee_name is not None:
            queryset = queryset.filter(employee_name=employee_name)
        if leave_type is not None:
            queryset = queryset.filter(leave_type=leave_type)
        return queryset
  
       
class LeaveRequestViewSet(viewsets.ModelViewSet):
    # authentication_classes = [authentication .TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsManager]
    
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    
    def approve(self, request, pk=None):
        
        leave_request = self.get_object()
        leave_request.leave_status = "Approved"
        if leave_request.leave_status == "Approved":
            leave_request.cancel_reason = "It is approved"
        employee_counts = LeaveRequest.objects.filter(leave_status="Approved").values('employee_name').annotate(request_count=Count('employee_name'))
        
        if len(employee_counts)>3:
            leave_request.lop_status = True
        else:
            leave_request.lop_status = False
        leave_request.save()
        serializer = self.get_serializer(leave_request)
        return Response(serializer.data)

    def cancel(self, request, pk=None):
        leave_request = self.get_object()
        leave_request.leave_status = "Cancelled"
        leave_request.cancel_reason = request.data.get('cancel_reason')
        employee_counts = LeaveRequest.objects.filter(leave_status="Approved").values('employee_name').annotate(request_count=Count('employee_name'))
        
        if len(employee_counts)>3:
            leave_request.lop_status = True
        else:
            leave_request.lop_status = False
        leave_request.save()
        serializer = self.get_serializer(leave_request)
        return Response(serializer.data)