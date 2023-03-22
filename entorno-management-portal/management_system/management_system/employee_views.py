from django.shortcuts import redirect, render

def HOME(request):
    return render (request, 'Employee/home.html')
