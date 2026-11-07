from django import forms

class confirmEmail(forms.Form):

    code = forms.CharField(max_length=10, required=True, label="Code")

    

