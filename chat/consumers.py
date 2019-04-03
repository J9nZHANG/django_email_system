# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def receive(self, data):
        self.send(data = json.dump({
            'message': "Y"
            }))