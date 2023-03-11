from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import myserializer   
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student_create(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serialzer=myserializer(pythondata)
        
        if serialzer.is_valid():
            serialzer.save()
            res= {'msg':'Data created !!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = 'application/json')
        
    json_data=JSONRenderer().render(serialzer.errors)

    return HttpResponse(json_data , content_type='application/json')