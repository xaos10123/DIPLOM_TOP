import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CouriersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("couriers", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("couriers", self.channel_name)

    async def new_order(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
