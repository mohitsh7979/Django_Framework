from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import *


def myform(request):
    if request.method=="POST":
        a=details(request.POST)
        if a.is_valid():
            name=a.cleaned_data['name']
            # fname=a.cleaned_data['fname']
            skill=a.cleaned_data['skill']
            address=a.cleaned_data['address']
            work=a.cleaned_data['work_experience']
            projects=a.cleaned_data['projects']
            certificates=a.cleaned_data['certificates']
            language=a.cleaned_data['language']
            # intrests=a.cleaned_data['intrests']
            mobile=a.cleaned_data['mobile']
            objective=a.cleaned_data['objective']
            email=a.cleaned_data['Email_id']
            dob=a.cleaned_data['dob']
            user=Resume(name=name,skill=skill,address=address, work_experience=work,projects=projects,certificates=certificates,language=language,
            mobile_no=mobile,objective=objective,email=email,Dob=dob)
            user.save()
            return HttpResponse('your details succefull added')

    else:

     a=details(auto_id="mohit",label_suffix="-",initial={'name':'Rohit'})
     a.order_fields(field_order=['Email_id','name'])
    context={
        'a':a
    }

    return render(request,'index.html',context)


def resume(request):
   collect=Resume.objects.all()
   print(collect)
   return render(request,'resume.html',{'collect':collect})


# Create your views here.

def user(request):
    if request.method=="POST":
        a=myuser(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse("Your account succefull created !")
    else:
     a=myuser()
    context={
        'a':a
    }
    return render(request,'usercreate.html',context)

def loginhandle(request):
    if request.method=="POST":
        b=AuthenticationForm(request=request, data=request.POST)
        if b.is_valid():
            myuser=b.cleaned_data['username']
            print(myuser)
            psd=b.cleaned_data['password']
            print(psd)
            user=authenticate(username=myuser,password=psd)
            if user is not None:
                login(request,user)
                return HttpResponse("you are successfull login")
    else:
           
     b=AuthenticationForm()
    context={
        'b':b
    }
    return render(request,'login.html',context)

def logouthandle(request):
    logout(request)
    return render(request,'index.html')


def list(request):
    data=Resume.objects.all()
    return render(request,'list.html',{'data':data})

def delete(request,name):
    data=Resume.objects.filter(name=name)
    data.delete()
    return redirect("/list/")