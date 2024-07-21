# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GroupNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.group_name = f'group_{self.group_id}'

        # Join the group channel
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group channel
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def user_joined(self, event):
        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
