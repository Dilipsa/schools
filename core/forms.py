from .models import Taker, Donate,Volunteer, Feedback
from django import forms



class TakerForm(forms.ModelForm):
    class Meta:
        model = Taker
        fields = "__all__"
        exclude = ["user", "approve"]

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['donation_amount']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['donation_thing']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']

