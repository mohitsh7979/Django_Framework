from django.shortcuts import render, redirect
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

def VIEW_FARMER(request):   
    return render(request,'Admin/view_farmer.html')

def VIEW_DEALER(request):
    return render(request,'Admin/view_dealer.html')

def VIEW_DISTRIBUTOR(request):
    return render(request,'Admin/view_distributor.html')
