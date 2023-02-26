from django.shortcuts import render, HttpResponse,redirect
from .forms import Myuserform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login


# Create your views here.

def myform(request):

    if request.method == "POST":
        a = Myuserform(request.POST)
        print(a)

        if a.is_valid():
            a.save()
            return HttpResponse("Your account succefully created !!!!")
        
    a = Myuserform()
    
    return render(request, 'user.html', {'a': a})

def authform(request):
    if request.method=="POST":
        a=AuthenticationForm(data=request.POST)

        if a.is_valid():
            uname=a.cleaned_data["username"]
            print(uname)
            upass=a.cleaned_data["password"]
            print(upass)

            a = authenticate(username=uname,password=upass)
            print(a)

            if a is not None:
                login(request,a)
                return redirect("/login/")



           
    a=AuthenticationForm()
    return render(request,'auth.html',{'a':a})