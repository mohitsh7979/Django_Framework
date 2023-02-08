from django.shortcuts import render
from .models import Student

# Create your views here.

def index(request,m=1):
    a=Student.objects.filter(id=1)
    print(a)
    for i in a:
        print(type(i.name))
      
    return render(request,'index.html')

