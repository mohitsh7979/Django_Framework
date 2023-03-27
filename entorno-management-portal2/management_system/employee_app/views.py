from django.shortcuts import render,redirect
from .forms import employee_form
from .models import Employee_model

# Create your views here.


def employee(request):
    if request.method == "POST":

        a = employee_form(request.POST,request.FILES)

        if a.is_valid():
            a.save()
            return redirect('/Admin/emp/employee_details/')
        
    a = employee_form()
    return render(request,'employee/home.html',{'a':a})

def employee_details(request):
     
    data = Employee_model.objects.all()

    return render(request,'employee/view_employee.html',{'data':data})


def employee_update(request , id):

    data = Employee_model.objects.filter(id=id)
     

    return render(request,'employee/update_employee.html',{'data':data})

def employee_delete(request , id):

    data = Employee_model.objects.filter(id=id)
    data.delete()
     

    return redirect('/Admin/emp/employee_details/')