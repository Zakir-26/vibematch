from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("suggestions/", views.username_suggestions, name="username_suggestion"),
    path("<str:username>", views.profile, name="profile"),

]