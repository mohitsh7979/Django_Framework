from django.shortcuts import render,HttpResponse
from .models  import student
from .serializers import Studentserializer
from rest_framework.renderers import JSONRenderer   

# Create your views here.

def myserailizer(request,a):
    data=student.objects.all()
    # data=student.objects.get(id=a)
    serializer_data=Studentserializer(data,many=True)
    json_data=JSONRenderer().render(serializer_data.data)
    print("This is json data :",json_data)
    print("type of data",type(json_data))
    print(data)
    print(serializer_data)

    return HttpResponse(json_data , content_type='application/json')

