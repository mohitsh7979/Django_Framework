import json

from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

from .models import *

class Mysynconsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("websocket conecting ....",event)
        print('channel layer ...',self.channel_layer)
        print('channel layer name...',self.channel_name)
        # print('group ka name',self.scope['url_route']['kwargs']['groupname'])
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        print(self.group_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print('websocket Received ...',event['text'])
        print(event['text'])
        print(type(event['text']))
        data=json.loads(event['text'])
        print("real data",data)
        print("print type of data",type(data))
        print(data['msg'])
        print(self.scope['user'])
        group=Group.objects.get(chatgroup=self.group_name)
        if self.scope['user'].is_authenticated:
          chat=Chat(
            content=data['msg'],
            group=group
          )
          chat.save()
          async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type':'chat.message',
            'message':event['text']
          })

        else:
            self.send({
                'type':'websocket.send',
                'text':json.dumps({"msg":"Login Required"})
            })

    def chat_message(self,event):
        print("Evnet message...",event)
        print("Evnet message...",event['message'])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
        

    def websocket_disconnect(self,event):
        print('channel layer ...',self.channel_layer)
        print('channel layer...',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        print("websocket disconnect...",event)
        raise StopConsumer

class Myaynconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("websocket conecting ....",event)
        print('channel layer ...',self.channel_layer)
        print('channel layer name...',self.channel_name)
        await self.channel_layer.group_add('programmers',self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self,event):
        print('websocket Received ...',event)
        print(event['text'])
        print(type(event['text']))
        await self.channel_layer.group_send('programmers',{
            'type':'chat.message',
            'message':event['text']
        })

    async def chat_message(self,event):
        print("Evnet message...",event)
        print("Evnet message...",event['message'])
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
        

    async def websocket_disconnect(self,event):
        print('channel layer ...',self.channel_layer)
        print('channel layer...',self.channel_name)
        await self.channel_layer.group_discard('programmers',self.channel_name)
        print("websocket disconnect...",event)
        raise StopConsumer