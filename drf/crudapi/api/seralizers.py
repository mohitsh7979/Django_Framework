from rest_framework import serializers
from .models import Student

class studentseralizer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    roll=serializers.IntegerField()
    address=serializers.CharField(max_length=30)


    def create(self , validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self , instance , validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.roll = validated_data.get('roll' , instance.roll)
        instance.address = validated_data.get('name' , instance.address)
