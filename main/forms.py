from django import forms
from .models import Profile, PartnerPref, Contact

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            "placeholder": "Enter your full name"
        })

        self.fields["age"].widget.attrs.update({
            "placeholder": "e.g. 18"
        })

        self.fields["city"].widget.attrs.update({
            "placeholder": "e.g. Mumbai"
        })

        self.fields["country"].widget.attrs.update({
            "placeholder": "e.g. India"
        })

        self.fields["profession"].widget.attrs.update({
            "placeholder": "e.g. Software Engineer"
        })

        self.fields["qualification"].widget.attrs.update({
            "placeholder": "e.g. Bachelor's Degree"
        })

        self.fields["height"].widget.attrs.update({
            "placeholder": "e.g. 175cm"
        })

        self.fields["min_age"].widget.attrs.update({
            "placeholder": "e.g 18"
        })

        self.fields["max_age"].widget.attrs.update({
            "placeholder": "e.g 38"
        })

        self.fields["partner_city"].widget.attrs.update({
            "placeholder": ""
        })
        

        self.fields["socialID"].widget.attrs.update({
            "placeholder": "e.g https://www.instagram.com/username"
        })

        self.fields["bio"].widget.attrs.update({
            "placeholder": "Tell people a little about yourself, not more then 500 characters"
        })


class PartnerPrefForm(forms.ModelForm):
    class Meta:
        model = PartnerPref
        fields = "__all__"
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["min_age"].widget.attrs.update({
            "placeholder": "e.g 18"
        })

        self.fields["max_age"].widget.attrs.update({
            "placeholder": "e.g 45"
        })

        self.fields["requirements"].widget.attrs.update({
            "placeholder": "Tell us about your ideal match, not more then 500 characters"
        })


class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["Full_Name"].widget.attrs.update({
            "placeholder": "full name"
        })

        self.fields["email"].widget.attrs.update({
            "placeholder": "email id"
        })

        self.fields["message"].widget.attrs.update({
            "placeholder": "Tell us how we can help, under 700 characters..."
        })
        