from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #inherit from django's usercreationform to add more fields
    email = forms.EmailField()

    class Meta:
        model = User #create a new User object when the form validates
        fields = ['username', 'email', 'password1', 'password2'] #the fields that will be displayed on the form

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User #create a new User object when the form validates
        fields = ['username', 'email'] #the fields that will be displayed on the form

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile #create a new User object when the form validates
        fields = ['image'] #the fields that will be displayed on the form
