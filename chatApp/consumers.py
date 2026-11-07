from .models import Chats, Room
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket connect---", event)
        print("scope user", self.scope['user'])

        self.room_name = self.scope['url_route']['kwargs']['roomkanaam']

        print("room name in connect--", self.room_name)

        self.room = await database_sync_to_async(Room.objects.get)(name=self.room_name)

        print("name of room is", self.room)

        self.current_user = self.scope['user'].id

        user1, user2 = map(int, self.room_name.split("_"))

        if user1 == self.current_user:
            self.receiver_user = user2
        elif user2 == self.current_user:
            self.receiver_user = user1
        else:
            await self.close()
            return

        print("self current user and self receiver user---", self.current_user, self.receiver_user)

        

        self.group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name

        )

        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("message received---", event)

        loadeddata = json.loads(event['text'])

        print("loadeddata is ---", loadeddata)

        print("actual loadeddata is ---", loadeddata['msg'])

        data = loadeddata['msg']

        chat = Chats(
            sender_id = self.current_user,
            receiver_id = self.receiver_user,
            content = data,
            room = self.room

        )

        await database_sync_to_async(chat.save)()

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'message': event['text'],
                'sender': self.current_user
            }
        )

    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'message': event['message'],
                'sender': event['sender']
            })
        })

    async def websocket_disconnect(self, event):
        print("websocket, disconnected---", event)
        

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )