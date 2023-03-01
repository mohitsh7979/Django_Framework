from django.shortcuts import render,HttpResponse
from myapp2.models import mymodel

# Create your views here.


def home(request):
    return HttpResponse("This is my app 2")


def mydata(request,a):
    # a=mymodel.objects.all()
    b=mymodel.objects.filter(id=a)
    b.delete()
    # print("This is my all data ",a)
    print("id 2 data ",b)
    return HttpResponse("this is my object")

