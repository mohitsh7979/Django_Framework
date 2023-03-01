from django.shortcuts import render, redirect, HttpResponse
from .forms import usercreationforms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm ,SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def myform(request):

    if request.method == "POST":
        a = usercreationforms(request.POST)

        if a.is_valid():
            a.save()

            return redirect("/")

    else:
        a = usercreationforms()
    return render(request, 'user.html', {'a': a})


def loginform(request):

    if request.method == "POST":
        a = AuthenticationForm(data=request.POST)

        if a.is_valid():
            uname = a.cleaned_data['username']
            upass = a.cleaned_data['password']

            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)

                messages.add_message(request,messages.SUCCESS,'your account has been created !!!')

    a = AuthenticationForm()

    return render(request, 'login.html', {'a': a})


def passchange(request):

    if request.method == "POST":
        a = PasswordChangeForm(user=request.user, data=request.POST)
        print("this is my ",a)

        if a.is_valid():
            print("This is valid")
            a.save()

            return HttpResponse("Your password successfully saved !!!!")

    a = PasswordChangeForm(user=request.user)
    return render(request, 'passwordchange.html', {'a': a})


def passreset(request):

    if request.method == "POST":
        a = SetPasswordForm(user=request.user, data=request.POST)
        print("this is my ",a)

        if a.is_valid():
            print("This is valid")
            a.save()

            return HttpResponse("Your password successfully saved !!!!")

    a = SetPasswordForm(user=request.user)
    return render(request,'reset.html',{'a':a})



def logouthandle(request):
    logout(request)
    return render(request, 'login.html')
