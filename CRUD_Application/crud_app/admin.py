from django.contrib import admin
from .models import Employee



@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display=['first_name','last_name','email','gender','mobile']
# Register your models here.
