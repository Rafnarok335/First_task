from django.db import models
from uuid import uuid4
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class User(AbstractUser):
        is_employee = models.BooleanField(default=False)
        is_manager = models.BooleanField(default=False)

## This is the employee table where i store the employee details with the fields here. I kept field here minimum.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='employee')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_of_joining = models.DateField()
    def __str__(self):
        return self.user.username

# This is the manager of an individual who represents their company and handles the assets.
class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='manager')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    
    company = models.CharField(max_length=100)
    def __str__(self):  
        return self.user.username


# class ManagerForm(ModelForm):
#     class Meta:
#         model = Manager
#         fields = ['name','username','email','phone','address','department','salary','company']


#         def __init__(self, *args, **kwargs):
#             super(ManagerForm, self).__init__(*args, **kwargs)






# Create your models here.

## This is the assets model where assets are stored with respectable information
class Assets(models.Model):
    asset_id = models.IntegerField(primary_key=True)
    asset_name = models.CharField(max_length=30)
    asset_type = models.CharField(max_length=30)
    asset_price = models.IntegerField()
    asset_purchase_date = models.DateField()
    asset_warranty = models.IntegerField()
    asset_status = models.CharField(max_length=30)
    asset_location = models.CharField(max_length=30)
    asset_description = models.CharField(max_length=30)
    def __str__(self):
        return self.asset_name

# This is the Key model where assets are assigned to manager model.
class AssetAssign(models.Model):
    asset_id = models.ForeignKey(Assets, on_delete=models.CASCADE)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset_assign_date = models.DateField()
    asset_return_date = models.DateField()
    asset_assign_status = models.CharField(max_length=30)
    asset_log = models.CharField(max_length=30)
    def __str__(self):
        return self.asset_assign_status