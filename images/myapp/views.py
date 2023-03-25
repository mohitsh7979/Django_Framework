from django.shortcuts import render,HttpResponse
from .forms import imageforms

# Create your views here.


def image(request):

    if request.method == "POST":

        print("i am in enter")
        
        data = imageforms(request.POST,request.FILES)


        print(data)

        if data.is_valid():

            print(" i am enter in if")

            data.save() 

            print("data is saved !!")

            return HttpResponse("data saved !!")

        
    
    else:

        data = imageforms()

    return render(request,'data.html',{'d':data})
