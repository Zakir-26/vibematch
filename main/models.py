from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
GENDER = [
    ("M", "Male"),
    ("F", "Female"),
    ("N", "Prefer not to say"),
]
PARTNER_PREF = [
    ("M", "Male"),
    ("F", "Female"),
    ("ANY", "Any one"),
]
PURPOSE = [
    ("Friendship", "Just for Friendship"),
    ("Serious", "Looking for serious life partner"),
    ("CASUAL", "Just Cascual Relationship calling, chatting nothing else"),
    ("Sexual", "Romantic Relationship, hangouts and more"),
    
]

PERSONALITY = [
    ("I", "Introvert"),
    ("E", "Extrovert"),
    ("A", "Ambivert"),
]
WORKOUT = [
    ("R", "Regularly"),
    ("S", "Sometimes"),
    ("N", "No Workout"),
]
SMOKING = [
    ("N", "Never"),
    ("S", "Sometimes"),
    ("R", "Regularly"),
]

RELIGION = [
    ("I", "Islam"),
    ("H", "Hinduism"),
    ("C", "Christanity"),
    ("B", "Budhasim"),
    ("J", "Jew"),
    ("A", "Atheism"),
    ("NO", "Don't want to say"),
]

PARTNER_CITY = [
    ("same_city", "City I live in"),
    ("same_state", "Anywhere in my State"),
    ("same_country", "Anywhere in my Country"),
    ("worldwide", "Anywhere in the World"),
    ("no_prefrence", "Location Doesn't Matter"),
]

RELATIONSHIP_GOAL = [
    ("marriage", "Marriage"),
    ("friendship", "Friendship"),
    ("serious", "Serious Relationship"),
    ("cacual", "Casual Dating"),
]

PREFFERED_RELIGION = [
    ("I", "Islam"),
    ("H", "Hinduism"),
    ("C", "Christanity"),
    ("B", "Budhasim"),
    ("J", "Jew"),
    ("A", "Atheism"),
    ("any", "Any Religion"),
    ("Doesn't matter", "Religion Doesn't Matter"),
]

PREFFERED_PROFESSION = [
    ("any", "Any"),
    ("govt job", "Government Job"),
    ("private job", "Private Job"),
    ("business", "Business"),
    ("student", "Student"),
    ("self E", "Self Employed"),
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    age = models.PositiveIntegerField( validators=[MinValueValidator(18)])
    gender = models.CharField(max_length=1, choices= GENDER)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    personality = models.CharField(max_length=1, choices=PERSONALITY)
    workout = models.CharField(max_length=1, choices=WORKOUT)
    height = models.PositiveSmallIntegerField(validators=[MinValueValidator(120), MaxValueValidator(210)])
    smoking = models.CharField(max_length=1, choices=SMOKING)
    religion = models.CharField(max_length=2, choices=RELIGION)
    looking_for = models.CharField(max_length=3, choices=PARTNER_PREF)
    purpose = models.CharField(max_length=11, choices=PURPOSE)
    min_age = models.PositiveIntegerField( validators=[MinValueValidator(18)])
    max_age = models.PositiveIntegerField( validators=[MinValueValidator(18)])
    partner_city = models.CharField(max_length=40, choices=PARTNER_CITY)
    socialID = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", default="profiles/default.png", blank=True, null=True)


    def __str__(self):
        return f"{self.name}"


class PartnerPref(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=3, choices=PARTNER_PREF)
    min_age = models.PositiveIntegerField(validators= [MinValueValidator(18)])
    max_age = models.PositiveIntegerField(validators= [MinValueValidator(18), MaxValueValidator(100)])
    city = models.CharField(max_length=40, choices=PARTNER_CITY)
    relationship_goal = models.CharField(max_length=20, choices=RELATIONSHIP_GOAL)
    preffered_religion = models.CharField(max_length=18, choices=PREFFERED_RELIGION)
    preffered_profession = models.CharField(max_length=30, choices=PREFFERED_PROFESSION)
    requirements = models.TextField(max_length=500, blank= True, default= "Looking for an Ideal partner")

    def __str__(self):
        return f"{self.user}"


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=45)
    email = models.EmailField()
    message = models.TextField(max_length=700, default="")

    def __str__(self):
        return f"{self.Full_Name}"
        