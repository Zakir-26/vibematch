from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=22, unique=True)

    def __str__(self):
        return f"{self.name}"

class Chats(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_chats")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recv_chats")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}"