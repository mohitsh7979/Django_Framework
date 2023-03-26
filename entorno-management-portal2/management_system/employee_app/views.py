from django.shortcuts import render
from .forms import employee_form

# Create your views here.


def employee(request):
    if request.method == "POST":
        
        a = employee_form(request.POST , request.FILES)

        if a.is_valid():
            a.save()
            return render('/')
        
    a = employee_form()
    return render(request,'employee/home.html',{'a':a})
