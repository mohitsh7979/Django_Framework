from django.shortcuts import render,HttpResponse,redirect
from .models import Student
from .forms import listforms

# Create your views here.


def index(request):
    a = Student.objects.all()
    print(a)
    
    return render(request, 'index.html', {'a': a})


def list(request):

    a=Student.objects.all()
    print(a)

    if request.method == "POST":
        b = listforms(data=request.POST)

        if b.is_valid():
            name = b.cleaned_data['name']
            father = b.cleaned_data['father_name']
            roll_no = b.cleaned_data['roll_no']
            date = b.cleaned_data['date']
            Student(name=name, father_name=father,
                    roll_no=roll_no, date=date).save()
            
            return redirect("/list/")
    
    else:

     b = listforms()
    context = {
        'b': b,
        'a':a
    }

    return render(request, 'index.html', context)
