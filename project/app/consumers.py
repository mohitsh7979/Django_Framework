import json
from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
class Myconsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect..',event)
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self,event):
        print('websocket received...',event)
        print(event['text'])
        for i in range(50):
              self.send({
            'type':'websocket.send',
            # 'text':str(i)
            'text':json.dumps({'count':i})
        })
        sleep(1)

    def websocket_disconnect(self,event):
        print('websocket disconnect..',event)
        raise StopConsumer()
class Myasynconsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect..',event)
        await self.send({
            'type':'websocket.accept',
        })
    async def websocket_receive(self,event):
        print('websocket received...',event)
        print('websocket received...',event)
        print(event['text'])
        for i in range(10000):
              self.send({
            'type':'websocket.send',
            'text':str(i)
        })
        await asyncio.sleep(1)
    async def websocket_disconnect(self,event):
        print('websocket disconnect..',event)
        raise StopConsumer()