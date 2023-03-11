from rest_framework import serializers
from .models import deserailization


class myserializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    address=serializers.CharField(max_length=30)




    def create(self,vaildate_data):
        return deserailization.objects.create(**vaildate_data)