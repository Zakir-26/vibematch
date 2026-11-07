from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from main.models import Profile

# Create your views here.
app_name = "core"

def home(request):
    return render(request, "core/home.html")

def profile(request, username):

    user = User.objects.filter(username=username).first()

    if not user:
        return render(request, "core/profile.html", {"user_exists": False, "profile": None, "username": username})
    
    profile = Profile.objects.filter(user__username=username).first()

    return render(request, "core/profile.html", {"profile": profile, "user_exists": True, "username": username})


def username_suggestions(request):
    query = request.GET.get("q", "").strip()

    if not query:
        return JsonResponse([], safe=False)

    users = User.objects.filter(
        username__icontains=query).values("username")[:10]
    return JsonResponse(
        list(users), safe=False)