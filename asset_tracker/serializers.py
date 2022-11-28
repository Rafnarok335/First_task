from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Employee, Manager, Assets , AssetAssign


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    department = serializers.CharField(min_length=2)
    
    class Meta:
        model = Employee
        fields = (
            'emp_id',
            'user',
            'name',
            'username',
            'email',
            'phone',
            'department',
            'salary',
            'date_of_joining',
            )
        read_only_fields = ('user',)
        


# class BrandSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(min_length=2)
    
#     class Meta:
#         model = Brand
#         fields = (
#             'alias',
#             'name',
#             'slug',
#             'created_at',
#             'updated_at')
#         read_only_fields = (
#             'alias',
#             'created_at',
            # 'updated_at')


class ManagerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    company = serializers.CharField(min_length=2)
    
    class Meta:
        model = Manager
        fields = (
            'manager_id',
            'user',
            'name',
            'username',
            'email',
            'phone',
            'address',
            'department',
            'salary',
            'company',)
        read_only_fields = (
            'phone',
            'salary',
            'address',
            'department',)

class AssetsSerializer(serializers.ModelSerializer):
    asset_id = serializers.PrimaryKeyRelatedField(read_only=True)

    
    class Meta:
        model = Assets
        fields = (
            'asset_id',
            'asset_name',
            'asset_type',
            'asset_price',
            'asset_purchase_date',
            'asset_warranty',
            'asset_status',
            'asset_location',
            'asset_description',)
    

class AssetAssignSerializer():
    asset_assign = serializers.PrimaryKeyRelatedField(read_only=True)
    asset_assign_status = serializers.CharField(min_length=2)
    class Meta:
        model: AssetAssign
        fields = ('asset_assign_status','asset_id','emp_id',
        'asset_assign_date','asset_return_date','asset_log')
        read_only_fields = ('asset_assign_date','asset_return_date','asset_log')