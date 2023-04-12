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
from rest_framework import authentication, permissions
# Create your views here.

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
        # print(serializer)
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
    
class LeaveRequestFilterView(APIView):
    authentication_classes = [authentication .TokenAuthentication]
    permissions_classes = [permissions . IsAuthenticated]
    def get(self, request):
        leave_type = request.GET.get('leave_type', '')
        leave_requests = LeaveRequest.objects.filter(leave_type=leave_type)
        serializer = LeaveRequestSerializer(leave_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    