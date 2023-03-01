from django.shortcuts import render,HttpResponse
from dealer_app.models import *
from farmer_app.models import *

# Create your views here.

def search(request):
    if request.method=="POST":
        data=request.POST["search"]
        a=Dealer.objects.filter(Business_Name=data)
        b=Distributer.objects.filter(Business_Name=data)
        c=Farmer.objects.filter(Name=data)
         
        if len(a)!=0:
            return render(request,'dealer_search.html',{'a':a})
        
        if len(b)!=0:
            return render(request,'distributer_search.html',{'b':b})
        
        if len(c)!=0:
            return render(request,'farmer_search.html',{'c':c})

        else:
          return HttpResponse(" Data is not found ")
        
       
   



