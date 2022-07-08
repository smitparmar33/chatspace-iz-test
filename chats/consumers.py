import json
from platform import platform
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chats.models import ChatModel
from django.contrib.auth import get_user_model

User = get_user_model()

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print('Room_Name',self.room_name)
      
        self.room_group_name = '%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        
        await self.accept()
        print("connected")


    async def receive(self, text_data=None, bytes_data=None):
        print("receiver")
        text_data_json = json.loads(text_data)
        sender =  text_data_json['sender']
        print("sender",sender)
        receiver =  text_data_json['receiver']
        print("receiver",receiver)
        message =  text_data_json['message']
        print("message",message)
        message_type = text_data_json['message_type']
        print("message_type",message_type)
        platform_name = text_data_json['platform_name']
        print("platform_name",platform_name)

        await self.save_message(sender,receiver,message,message_type,platform_name)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender':sender,
                'receiver':receiver,
                'message': message,
                'message_type':message_type,
                'platform_name':platform_name
            }
        )

    async def chat_message(self, event):
        print("chat_message")
        sender = event['sender']
        receiver = event['receiver']
        message = event['message']
        message_type = event['message_type']
        platform_name = event['platform_name']

        print("sender",sender)
        print("receiver",receiver)
        print("message",message)
        print("message_type",message_type)
        print("platform_name",platform_name)


        await self.send(text_data=json.dumps({
            'sender': sender,
            'receiver':receiver,
            'message': message,
            'message_type':message_type,
            'platform_name':platform_name
        }))
        print("send")

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_message(self,sender,receiver,message,message_type,platform_name):
        ChatModel.objects.create(
            sender = sender , receiver = receiver,
            message = message , message_type = message_type ,
            platform_name = platform_name, room_name = self.room_group_name)
