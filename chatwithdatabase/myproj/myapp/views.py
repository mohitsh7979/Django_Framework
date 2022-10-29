
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request,group_name):
    groupName=Group.objects.filter(chatgroup=group_name).first()
    chats=[]
    if groupName:
        chats=Chat.objects.filter(group=groupName)
        print(chats)
    else:
       groupName=Group(chatgroup=group_name)
       groupName.save()
    return render(request,'index.html',{'group_name':group_name,'chats':chats})