from django.shortcuts import render,HttpResponse
from .forms import *
from .models import *



def myform(request):
    if request.method=="POST":
        a=details(request.POST)
        if a.is_valid():
            name=a.cleaned_data['name']
            skill=a.cleaned_data['skill']
            address=a.cleaned_data['address']
            work=a.cleaned_data['work_experience']
            projects=a.cleaned_data['projects']
            certificates=a.cleaned_data['certificates']
            language=a.cleaned_data['language']
            intrests=a.cleaned_data['intrests']
            user=Resume(name=name,skill=skill,address=address, work_experience=work,projects=projects,certificates=certificates,language=language,intrests=intrests)
            user.save()
            return HttpResponse('your details succefull added')

    else:

     a=details()
    context={
        'a':a
    }

    return render(request,'index.html',context)


def resume(request):
   collect=Resume.objects.all()
   print(collect)
   return render(request,'resume.html',{'collect':collect})


# Create your views here.
