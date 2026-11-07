from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name = "home"),
    path("find-my-match", views.userInfo, name="userinfo"),
    path("find-my-match/2", views.partnerPref, name="partnerpref"),
    path("done", views.done, name="done"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("privacy-policy", views.privacy, name="privacy"),
    path("browse-men", views.BrowseMen, name="browseMen"),
    path("browse-women", views.BrowseWomen, name="browseWomen"),
    path("browse", views.browse, name="browse")
]