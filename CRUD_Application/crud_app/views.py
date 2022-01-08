from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import employee_registration_form
from .models import Employee
from django.contrib import messages
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
            messages.success(request, 'Employee Profile details Save.')
            emp_reg_form=employee_registration_form()
    emp = Employee.objects.all()
        
    return render(request,"crud_app/index.html",{'form':emp_reg_form,'employeeList':emp})

def update_data(request,id):
    template_name="crud_app/update_Employee.html"
    emp_obj = Employee.objects.get(pk=id)
    if request.method == 'POST':
        fm=employee_registration_form(request.POST,instance=emp_obj)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Employee Profile details Update.')

            return HttpResponseRedirect('/')
    else:
        fm=employee_registration_form(instance=emp_obj)

    return render(request, template_name,{'form':fm})

def delete_record(request,id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        pi.delete()
        messages.warning(request, 'Employee Profile Delete.')

    return HttpResponseRedirect('/')
