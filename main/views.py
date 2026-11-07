from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserInfoForm, PartnerPrefForm, Contact

# Create your views here.

def home(request):
    return render (request, "main/index.html")


@login_required
def userInfo(request):
    form = UserInfoForm()
    if request.method == "POST":
        form = UserInfoForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("main:done")
    return render (request, "main/info.html", {"form" : form})


@login_required
def partnerPref(request):
    form = PartnerPrefForm()
    if request.method == "POST":
        form = PartnerPrefForm(request.POST)

        if form.is_valid():
            partner = form.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect("main:done")

    return render (request, "main/partnerpref.html", {"form" : form})


@login_required
def done(request):
    return render(request, "main/done.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    form = Contact()

    if request.method == "POST":
        form = Contact(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect("main:thankyou")

    return render(request, "main/contact.html", {"form": form})

def thankyou(request):
    return render(request, "main/thankyou.html")

def privacy(request):
    return render(request, "main/privacy.html")


@login_required
def browse(request):
    return render(request, "main/browse.html")

def BrowseMen(request):
    men = Profile.objects.filter(gender="M").order_by("?")

    return render(request, "main/browse-men.html", {"men": men})

def BrowseWomen(request):
    women = Profile.objects.filter(gender="F").order_by("?")

    return render(request, "main/browse-women.html", {"women": women})