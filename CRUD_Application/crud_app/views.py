from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import employee_registration_form
from .models import Employee
# Create your views here.

def home(request):

    emp_reg_form = employee_registration_form()
    if request.POST:
        emp_reg_form = employee_registration_form(request.POST)
        print(request.POST['gender'])
        if (emp_reg_form.is_valid()):
            print(request.POST['gender'])
            fn=emp_reg_form.cleaned_data['first_name']
            ln=emp_reg_form.cleaned_data['last_name']
            email=emp_reg_form.cleaned_data['email']
            mobile=emp_reg_form.cleaned_data['mobile']
            gender=emp_reg_form.cleaned_data['gender']
            reg=Employee(first_name=fn,last_name=ln,email=email,mobile=mobile,gender=gender)
            reg.save()
            emp_reg_form=employee_registration_form()
    emp = Employee.objects.all()
        
    return render(request,"crud_app/index.html",{'form':emp_reg_form,'employeeList':emp})

def delete_record(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
