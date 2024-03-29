from django.shortcuts import render, redirect, HttpResponse
from .forms import DealerForm, DistributerForm
from .models import Dealer, Distributer

# Create your views here.


def dealer(request):

    b = Dealer.objects.all()
    return render(request, 'dealer/dealer_table.html', {'b': b})


def dealer_form(request):
    if request.method == "POST":
        a = DealerForm(data=request.POST)

        print(a)

        if a.is_valid():
            Bname = a.cleaned_data["Business_Name"]
            MNo = a.cleaned_data["Mobile_No"]
            WNo = a.cleaned_data["Whatsapp_No"]
            Ad = a.cleaned_data["Address"]
            Dis = a.cleaned_data["District"]
            Pc = a.cleaned_data["Pin_code"]
            GNo = a.cleaned_data["Gst_No"]
            SL = a.cleaned_data["Seed_License"]
            Dealer(Business_Name=Bname, Mobile_No=MNo, Whatsapp_No=WNo,
                   Address=Ad, District=Dis, Pin_code=Pc, Gst_No=GNo, Seed_License=SL).save()
            return redirect("/deal/dealer_detail/")
    else:
        a = DealerForm()

    return render(request, 'dealer/dealer_form.html', {'a': a})


def delete_data(request, id):
    delete_data = Dealer.objects.filter(id=id)
    delete_data.delete()
    return redirect("/deal/dealer_detail/")


def update_data(request, id):
    if request.method == "POST":
        form_data = DealerForm(request.POST)
        data = Dealer.objects.filter(id=id)
        if form_data.is_valid():
            for i in data:
                i.Business_Name = form_data.cleaned_data["Business_Name"]
                i.Mobile_No = form_data.cleaned_data["Mobile_No"]
                i.Whatsapp_No = form_data.cleaned_data["Whatsapp_No"]
                i.Address = form_data.cleaned_data["Address"]
                i.District = form_data.cleaned_data["District"]
                i.Pin_code = form_data.cleaned_data["Pin_code"]
                i.Gst_No = form_data.cleaned_data["Gst_No"]
                i.Seed_License = form_data.cleaned_data["Seed_License"]
                i.save()
                return redirect("/deal/dealer_detail/")

    data = Dealer.objects.filter(id=id)

    return render(request, 'dealer/dealer_detail_update.html', {'a': data})


def Distributers(request):
    if request.method == "POST":
        a = DistributerForm(data=request.POST)

        print(a)

        if a.is_valid():
            usr = a.cleaned_data["user"]
            Bname = a.cleaned_data["Business_Name"]
            MNo = a.cleaned_data["Mobile_No"]
            WNo = a.cleaned_data["Whatsapp_No"]
            Ad = a.cleaned_data["Address"]
            Dis = a.cleaned_data["District"]
            Pc = a.cleaned_data["Pin_code"]
            GNo = a.cleaned_data["Gst_No"]
            SL = a.cleaned_data["Seed_License"]
            Distributer(user=usr, Business_Name=Bname, Mobile_No=MNo, Whatsapp_No=WNo,
                        Address=Ad, District=Dis, Pin_code=Pc, Gst_No=GNo, Seed_License=SL).save()
            return redirect("/deal/distributer_detail/")

    a = DistributerForm()
    return render(request, 'dealer/distributer.html', {'a': a})


def distributer_object(request):
    b = Distributer.objects.all()
    return render(request, 'dealer/distributer_table.html', {'b': b})


def Distributer_delete_data(request, id):
    delete_data = Distributer.objects.filter(id=id)
    delete_data.delete()
    return redirect("/deal/distributer_detail/")


def Distributer_update_data(request, id):
    if request.method == "POST":
        form_data = DistributerForm(request.POST)
        data = Distributer.objects.filter(id=id)
        if form_data.is_valid():
            for i in data:
                i.Business_Name = form_data.cleaned_data["Business_Name"]
                i.Mobile_No = form_data.cleaned_data["Mobile_No"]
                i.Whatsapp_No = form_data.cleaned_data["Whatsapp_No"]
                i.Address = form_data.cleaned_data["Address"]
                i.District = form_data.cleaned_data["District"]
                i.Pin_code = form_data.cleaned_data["Pin_code"]
                i.Gst_No = form_data.cleaned_data["Gst_No"]
                i.Seed_License = form_data.cleaned_data["Seed_License"]
                i.save()
                return redirect("/deal/distributer_detail/")

    data = Distributer.objects.filter(id=id)

    data1=DistributerForm()
    a=data1["user"]

    return render(request, 'dealer/distributer_detail_update.html', {'a': a})

