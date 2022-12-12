from django.shortcuts import render
from .models import *
# from .forms import Customer

# Create your views here.

def Customer(request):
    Customer_details=Customer(request.data)
    context={
        'Customer_details':Customer_details
        }
    return render(request,'customer.html',context)
