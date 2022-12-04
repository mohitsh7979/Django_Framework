from django.shortcuts import render,HttpResponse
from .forms import ResumeForm
from .models import *

# Create your views here.
def resume(request):
    if request.method=="POST":
        a=ResumeForm(request.POST,request.FILES)
        print(a)
        if a.is_valid():
            a.save()
            return HttpResponse("Your form is successfull Submited !")
    else:
     a=ResumeForm()
    
    
    context={
        'a':a,
        
    }
    return render(request,'resume.html',context)


