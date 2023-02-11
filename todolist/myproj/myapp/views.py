from django.shortcuts import render, redirect
from .forms import listforms
from .models import listmodel

# Create your views here


def list(request):
    data = listmodel.objects.all()
    # print(data)
    # if data==None:
    #     print("Mere pass kch nhi h")
    # for i in data:
    #     print(i.delete())

    if request.method == "POST":
        myform = listforms(data=request.POST)
        if myform.is_valid():
            name = myform.cleaned_data['name']
            email = myform.cleaned_data['email']
            course = myform.cleaned_data['course']
            listmodel(name=name, email=email, course=course).save()

            return redirect("/")
    else:

        myform = listforms() 
    return render(request, 'list.html', {'myform': myform, 'data': data})


def delete(request, id):
    deletedata = listmodel.objects.filter(id=id)
    for i in deletedata:
        print(i.delete())
    # deletedata.delete()
    return redirect("/")


def update(request, id):
    if request.method == "POST":
        data = listforms(data=request.POST)
        updatedata = listmodel.objects.filter(id=id)
        print(updatedata)
        if data.is_valid():
            for i in updatedata: 
                i.name = data.cleaned_data['name']
                i.email = data.cleaned_data['email']
                i.course = data.cleaned_data['course']
                i.save()

    return redirect("/")

def updatelist(request,id):
    a=id
    myform = listforms()
    return render(request,'updatelist.html',{'myform':myform,'a':a})