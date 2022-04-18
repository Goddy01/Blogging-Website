from dataclasses import fields
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django import forms


class UserForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'first_name', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')