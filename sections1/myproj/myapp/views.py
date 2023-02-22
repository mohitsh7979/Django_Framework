from django.shortcuts import render,HttpResponse
from .models import Farmer
# Create your views here.


def add(request):
    a=10
    b=20
    c=a+b

    return HttpResponse(c)

def minus(request):
    a=20
    b=10
    c=a-b
    return HttpResponse(c)

def abc(request):
    a=Farmer.objects.all()

    for i in a:
        i.name="rohit"
    

    context={
        'b':a
    }

    # for i in a:
    #     print(i.name)
    #     print(i.Father_name)
    #     print(i.mobile_no)
    # print("this is object",a)

    return render(request,'abc.html',context)




# def login(request):
#     return render(request,'login.html')