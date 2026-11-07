from django.urls import path
from . import views

urlpatterns = [
    path("", views.chatusers, name="chat_user"),
    path("<int:user_id>/", views.Chat, name="chat"),
    path("flirt/<int:user_id>/", views.Flirt, name="flirt"),
    
]