from django import forms
from .models import Register
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

