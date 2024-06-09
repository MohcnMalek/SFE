import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChargePointConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Process the received data here
        await self.send(text_data=json.dumps({
            'message': 'Data received',
        }))
