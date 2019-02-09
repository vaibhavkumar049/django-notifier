from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer

import asyncio

class NoisyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip",self.channel_name)
        print(f'Added {self.channel_name} channel to gossip')

    async def disconnect(self):
        await self.channel_layer.group_discard("gossip",self.channel_name)
        print(f'Removed {self.channel_name} channel to gossip')

    async def user_gossip(self,event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")





# class TickTockConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         while 1:
#             await asyncio.sleep(1)
#             await self.send_json("tock")
#             await asyncio.sleep(1)
#             await self.send_json("...............tok")



# class EchoConsumer(AsyncConsumer):

#     async def websocket_connect(self,event):
#         await self.send({
#             "type" : "websocket.accept"
#         })

#     async def websocket_receive(self, event):
#         await self.send({
#             "type" : "websocket.send",
#             "text" : event["text"]
#         })

