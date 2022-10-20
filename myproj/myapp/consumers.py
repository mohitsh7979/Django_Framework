from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

class MySynconsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connect ...',event)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self,event):
        print('websocket Received ...',event)

    def websocket_disconnect(self,event):
        print('websocket disconnected...',event)
        raise StopConsumer()
    

class myasynconsumer(AsyncConsumer):
   async def websocket_connect(self,event):
        print('websocket connected ....',event)
        await self.send({
            'type':'websocket.accept'
        })

   async def websocket_receive(self,event):
        print('websocket Received ...',event)

   async def websocket_disconnect(self,event):
        print('websocket disconnected...',event)
        raise StopConsumer()
        