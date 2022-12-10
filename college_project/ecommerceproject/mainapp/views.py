from django.shortcuts import render

# Create your views here.

def header(request):
    return render(request,'mainapp/e-commerce.html')
