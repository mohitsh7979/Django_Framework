from rest_framework import serializers


class Studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    address=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
