from django.shortcuts import render,HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# from .forms import Customer

# Create your views here.

def Customer_details(request):
  
    if request.method=="POST":
         a=customer(request.POST)
         if a.is_valid():
            usr=request.user
            print(usr)
            first_name=a.cleaned_data['First_name']
            last_name=a.cleaned_data['last_name']
            email=a.cleaned_data['Email_id']
            address=a.cleaned_data['address']
            land=a.cleaned_data['land_mark']
            state=a.cleaned_data['State']
            city=a.cleaned_data['City']
            pin=a.cleaned_data['pin_code']
            mobile=a.cleaned_data['Mobile_no']
            m=Customer(user=usr,First_name=first_name,last_name=last_name,Email_id=email,address=address,land_mark=land,State=state,City=city,pin_code=pin,Mobile_no=mobile)
            m.save()
            return HttpResponse("your account is created")
    else:
     a=customer()
    print(a)
    context={
        'a':a
        }
    return render(request,'authenticationapp/customer.html',context)


def register(request):
    if request.method=="POST":
        a=Register(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse("your account is created")
    else:
     a=Register()
    print(a)
    context={
        'a':a
        }
    return render(request,'authenticationapp/register.html',context)


def loginhandle(request):

      if request.method=="POST":
        # a=AuthenticationForm(request=request,data=request.POST)
        # if a.is_valid():
            uname=request.POST['username']
            pas=request.POST['password']
            print(uname)
            print(pas)
            user=authenticate(username=uname,password=pas)

            if user is not None:
                login(request,user)
            
      return render(request,'authenticationapp/login.html')
      

    # if request.method=="POST":
    #     a=AuthenticationForm(request=request,data=request.POST)
    #     if a.is_valid():
    #         uname=a.cleaned_data['username']
    #         pas=a.cleaned_data['password']
    #         print(uname)
    #         print(pas)
    #         user=authenticate(username=uname,password=pas)

    #         if user is not None:
    #             login(request,user)
            
    #         return HttpResponse("your are succefull login")
    # else:
    #  a=AuthenticationForm()
     
    
    # context={
    #     'a':a
    #     }
    


def profile_page(request):
    return render(request,'authenticationapp/profile.html')