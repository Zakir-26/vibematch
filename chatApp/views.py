from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Chats, Room
import random


# Create your views here.
@login_required
def Chat(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user == request.user:
        return HttpResponse("Error, you can't chat with yourself")
    
    room_name = f"{min(request.user.id, target_user.id)}_{max(request.user.id, target_user.id)}"

    try:   
        room = Room.objects.get(name=room_name)
        chats = Chats.objects.filter(room=room).order_by("timestamp")
    except Room.DoesNotExist:
        room = Room(name=room_name)
        room.save() 
        chats = []
    return render(request, "chatApp/chat.html", {"targetUser" : target_user, "roomName": room_name, "chats": chats})

@login_required
def chatusers(request):
    chats = Chats.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by("-timestamp")

    users = []

    for chat in chats:
        if chat.sender == request.user:
            other_user = chat.receiver
        else:
            other_user = chat.sender

        if other_user not in users:
            users.append(other_user)

    return render(request, "chatApp/chat_users.html", {"users": users})

@login_required
def Flirt(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    if target_user == request.user:
        return HttpResponse("Error! You can't flirt with yourself.")

    room_name = f"{min(request.user.id, target_user.id)}_{max(request.user.id, target_user.id)}"

    Flirting_Lines = [
        "😉 I couldn't scroll past your profile without saying hi.",
        "😉 Do you believe in love at first sight - or should I come to you again",
        "😉 Someone had to make the first move.",
        "😉 Are ur parents Artists? because you are a masterpiece",
        "😄 Is your name Wi-Fi? Because I am really feeling a connection",
        "😉 Are you French? Because Eiffel for you",
        "😉 No pen, no paper but you still draw my attention.",
        "😉 I'm lost. Can you give me directions to your heart?",
        "😉 Wanna be Minecraft without the craft?",
        "😄 Are you a time traveller? Because I can see you in my future",
        "😉 If you were a triangle you'd be acute one.",
        "😄 If I could rearrange the alphabet, I’d put U and I together",
        "😉 Consider this my way of saying hello.",
        "😄 I came here to browse, but your profile changed the plan.",
        "They say Dating is a numbers game, so can I get yours 😉",
        "4+4=8 but you+me=fate 😉",
        "Are you tired? You've been running through my mind all day. 😄",
        "😏 If profiles could make first moves, yours just did.",
        "✨ They say nothing lasts forever. Want to be my nothing?",
        "😏 I'll let the wink do the talking for now.",
        "Are you a parking ticket? Because you've got fine written all over you.✨",
        "✨I'm not a photographer, but I can picture us together.",
        "Are you a loan? You've got my interest.😉"
    ]

    Flirting_Line = random.choice(Flirting_Lines)

    try:   
        room = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        room = Room(name=room_name)
        room.save() 

    Chats.objects.create(
        sender = request.user,
        receiver = target_user,
        content = Flirting_Line,
        room = room
        )

    return redirect("chat", user_id=target_user.id)

    