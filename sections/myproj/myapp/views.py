from django.shortcuts import render,HttpResponse
from .models import Student
from .forms import listforms

# Create your views here.


def index(request):
    a = Student.objects.all()

    # context={

    #     'a':a
    # }
    return render(request, 'index.html', {'a': a})


def list(request):

    if request.method == "POST":
        b = listforms(data=request.POST)

        if b.is_valid():
            name = b.cleaned_data['name']
            father = b.cleaned_data['father_name']
            roll_no = b.cleaned_data['roll_no']
            date = b.cleaned_data['date']
            Student(name=name, father_name=father,
                    roll_no=roll_no, date=date).save()
            
            return HttpResponse("Your data is saved")
    
    else:

     b = listforms()
    context = {
        'b': b
    }

    return render(request, 'index.html', context)
