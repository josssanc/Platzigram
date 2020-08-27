"""Form update profile"""
#Dajango
from django import forms

from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(min_length=4,max_length=50)
    password = forms.CharField(max_length=70,widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70,widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2,max_length=50)
    last_name = forms.CharField(min_length=2,max_length=50)
    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())
    
    
    def clean_username(self):
        """Username must be unique"""
        self.cleaned_data['username']
        username_taken = User.object.filter(username=username).exist()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
    def clean(self):
        """Verify password confirmation mathc"""
        data = super().clean()

        password = data['password']
        passwrod_confirmation = data['password_confirmation']



class ProfileForm(forms.Form):
    """Profile form."""
    website = forms.URLField(max_length=200)
    biography = forms.CharField(max_length=500,required=False)
    phone_number = forms.CharField(max_length=20,required=False)
    picture = forms.ImageField()