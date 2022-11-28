from django.contrib import admin
from .models import Assets, Employee , AssetAssign, Manager
# Register your models here.
admin.site.register(Assets)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(AssetAssign)