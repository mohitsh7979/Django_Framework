from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import Auth,forms


# Create your views here.


def loginhandle(request):

    if request.method == "POST":
        a = AuthenticationForm(request=request, data=request.POST)

        if a.is_valid():
            uname = a.cleaned_data['username']
            passwd = a.cleaned_data['password']

            user = authenticate(username=uname, password=passwd)

            if user is not None:
                login(request, user)

            return redirect("/")

    a = AuthenticationForm()
    return render(request, 'authentication/login.html', {'a': a})


def signup(request):

    if request.method == "POST":
        b = Auth(data=request.POST)

        if b.is_valid():
            b.save()

            if b.is_valid():
               uname = b.cleaned_data['username']
               pas = b.cleaned_data['password1']
               print(uname)
               print(pas)
               user = authenticate(username=uname, password=pas)

               if user is not None:
                 login(request, user)

            return redirect("/")

            

    b = Auth()
    return render(request, 'authentication/signup.html', {'b': b})

def logouthandle(request):
    logout(request)
    return redirect("/")
