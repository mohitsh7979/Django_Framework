from django.shortcuts import render,HttpResponse
from .forms import *
from .models import *



def myform(request):
    if request.method=="POST":
        a=details(request.POST)
        if a.is_valid():
            name=a.cleaned_data['name']
            fname=a.cleaned_data['fname']
            skill=a.cleaned_data['skill']
            address=a.cleaned_data['address']
            work=a.cleaned_data['work_experience']
            projects=a.cleaned_data['projects']
            certificates=a.cleaned_data['certificates']
            language=a.cleaned_data['language']
            intrests=a.cleaned_data['intrests']
            mobile=a.cleaned_data['mobile']
            objective=a.cleaned_data['objective']
            email=a.cleaned_data['Email_id']
            dob=a.cleaned_data['dob']
            user=Resume(name=name,skill=skill,address=address, work_experience=work,projects=projects,certificates=certificates,language=language,intrests=intrests,
            fname=fname,mobile_no=mobile,objective=objective,email=email,Dob=dob)
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
