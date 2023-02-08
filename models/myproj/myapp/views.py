from django.shortcuts import render
from .models import Runner
# Create your views here.

def mymodels(request):
    data=Runner.objects.create(name='Mohit')
    print(data.name)
    data.clean()
    print("clear:",data.name)
    return render(request,'mymodels.html')
