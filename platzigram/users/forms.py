"""Form update profile"""
#Dajango
from django import forms

class ProfileForm(forms.Form):
    """Profile form."""
    website = forms.URLField(max_length=200)
    biography = forms.CharField(max_length=500,required=False)
    phone_number = forms.CharField(max_length=20,required=False)
    picture = forms.ImageField(

    )