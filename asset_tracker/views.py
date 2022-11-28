from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Assets, Employee , AssetAssign

from .serializers import EmployeeSerializer , AssetsSerializer ,AssetAssignSerializer


class AssetListView(generics.ListCreateAPIView):
    queryset = Assets.objects.filter()
    serializer_class = AssetsSerializer
    permission_class = [IsAdminUser]
    

class AssetAssignView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssetAssign.objects.filter()
    serializer_class = AssetAssignSerializer
    permission_class = [IsAdminUser]
    lookup_field = 'asset_id'


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.filter()
    serializer_class = EmployeeSerializer
    permission_class = [IsAdminUser]
    

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.filter()
    serializer_class = EmployeeSerializer
    permission_class = [IsAdminUser]
    lookup_field = 'emp_id'