from django.contrib import admin
from .models import Chats, Room

# Register your models here.

admin.site.register(Chats)
list_display = ['id', 'sender', 'receiver', 'content', 'timestamp', 'room']
admin.site.register(Room)