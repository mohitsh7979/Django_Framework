from django.shortcuts import render, HttpResponse, redirect
from .models import Farmer
from .forms import EmployeeForm

# Create your views here.


def farmer(request):
    if request.method=="POST":
        a=request.POST['search']
        all=Farmer.objects.filter(Name=a)
        return render(request,'index.html',{'all':all})
    
    all = Farmer.objects.all()


    return render(request, 'farmer/farmer_table.html', {'all': all})


# def updatelist(request,id):
#     model_data=Farmer.objects.filter(id=id)

#     print(model_data)
#     for i in model_data:
#         i.Name="xyz"
#         i.save()
#         print(i.Name)


def updatelist(request, id):
    if request.method == "POST":
        data = EmployeeForm(data=request.POST)
        updatedata = Farmer.objects.filter(id=id)
        print(updatedata)
        if data.is_valid():
            for i in updatedata:
                i.Name = data.cleaned_data['Name']
                i.Mobile_No = data.cleaned_data['Mobile_NO']
                i.Whatsapp_No = data.cleaned_data['Whatsapp_No']
                i.Village = data.cleaned_data['Village']
                i.District = data.cleaned_data['District']
                i.Pin_code = data.cleaned_data['Pin_code']
                i.save()

    return redirect("/")


def update(request, id):
    data = EmployeeForm()
    b=Farmer.objects.filter(id=id)
    for i in b:
        print(i.Name)
    # print("yes",b.Name)
    a = id

    return render(request, 'farmer/updatelist.html', {'data': data, 'a': a,'b':b})

def delete(request,id):
    delete_data=Farmer.objects.filter(id=id)
    delete_data.delete()
    return redirect("/")

def farmer_detail(request):

    if request.method == "POST":
        a = EmployeeForm(data=request.POST)

        if a.is_valid():
            Name = a.cleaned_data['Name']
            Mobile_No = a.cleaned_data['Mobile_NO']
            Whatsapp_No = a.cleaned_data['Whatsapp_No']
            Village = a.cleaned_data['Village']
            District = a.cleaned_data['District']
            Pin_code = a.cleaned_data['Pin_code']

            Farmer(Name=Name, Mobile_No=Mobile_No, Whatsapp_No=Whatsapp_No,
                   Village=Village, District=District, Pin_code=Pin_code).save()

            return redirect("/")

    a = EmployeeForm()

    return render(request, 'farmer/former_detail.html', { 'a': a})


def search(request):
    if request.method=="POST":
        a=request.POST['search']
        print(a)
        b=Farmer.objects.filter(Name=a)
        print(b)





