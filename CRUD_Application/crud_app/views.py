from django.shortcuts import render
from django.http import HttpResponse
from .forms import employee_registration_form
from .models import Employee
# Create your views here.

def home(request):

    emp_reg_form = employee_registration_form()
    if request.method == 'POST':
        emp_reg_form = employee_registration_form(instance=Employee)
        if (emp_reg_form.isvalid):
            emp_reg_form.save()
    return render(request,"crud_app/index.html",{'form':emp_reg_form})
