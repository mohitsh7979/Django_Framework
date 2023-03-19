from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from farmer_app.forms import EmployeeForm
from dealer_app.forms import DealerForm,DistributerForm
from dealer_app.models import Dealer,Distributer
from app.models import CustomUser
from app.models import Employee


@login_required(login_url='/')
def HOME(request):
    return render(request,'admin/home.html')

@login_required(login_url='/')
def ADD_FARMER(request):
    farmer = EmployeeForm()
    return render(request,'admin/add_farmer.html',{'farmer':farmer})

@login_required(login_url='/')
def ADD_DISTRIBUTOR(request):
    a = DealerForm()
    return render(request,'admin/add_distributor.html',{'a':a})

@login_required(login_url='/')
def ADD_DEALER(request):
    a = DistributerForm()
    return render(request,'admin/add_dealer.html',{'a':a})


def ADD_EMPLOYEE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_no = request.POST.get('mobile_no')
        gender =  request.POST.get('gender')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        pan_card = request.FILES.get('pan_card')
        adhar_card = request.FILES.get('adhar_card')
        cheque = request.FILES.get('cheque')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('add_employee')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('add_employee')
        
        else:
            user = CustomUser(profile_pic = profile_pic , first_name = first_name,
                                last_name = last_name, email=email, username=username,
                               user_type=2)
        
        user.set_password(password)
        user.save()

        employee = Employee(
            admin = user,
            address=address,
            gender =gender
        )
        employee.save()
        messages.success(request,'Employee is succesfully added!')
        return redirect('add_employee')
    return render(request,'admin/add_employee.html')

def VIEW_EMPLOYEE(request):
    return render(request,'admin/view_employee.html')

def VIEW_FARMER(request):   
    return render(request,'admin/view_farmer.html')

def VIEW_DEALER(request):
    return render(request,'admin/view_dealer.html')

def VIEW_DISTRIBUTOR(request):
    return render(request,'admin/view_distributor.html')

@login_required(login_url='/')
def RESOURCES(request):
    return render(request,'admin/resources.html')
    



