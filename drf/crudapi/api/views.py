from django.shortcuts import render,HttpResponse
from .models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .seralizers import studentseralizer
from rest_framework.renderers import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def studentapi(request):

    if request.method == 'GET':
        json_data = request.body
        print(" This is json data : ",json_data)
        stream = io.BytesIO(json_data)
        print("This is stream data : ", stream)
        # pythondata = JSONParser().parse(stream)
        pythondata = JSONParser().parse(stream)
        print("This is python data : ",pythondata)
        id = pythondata.get('id',None)
        print()
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = studentseralizer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type = 'application/json')
        
        stu = Student.objects.all()
        serailzer=studentseralizer(stu)
        json_data = JSONRenderer().render(serailzer.data)
        return HttpResponse(json_data , content_type = 'application/json')
    
    if request.method =="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serailzer = studentseralizer(data = pythondata)

        if serailzer.is_valid():
            serailzer.save()

            res = {'msg':'Data created'} 
            json_data = JSONRenderer().render(res)  
            return HttpResponse(json_data , content_type = 'application/json') 
        
        json_data = JSONRenderer().render(serailzer.errors)  
        return HttpResponse(json_data , content_type = 'application/json') 






