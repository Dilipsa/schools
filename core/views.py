from django.shortcuts import render, redirect, get_object_or_404
from .models import Donate, Taker, Volunteer, Feedback
from .forms import TakerForm, DonateForm, VolunteerForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import View, ListView
from account.forms import UserForm
from django.contrib.auth.models import User

def index_view(request):
    return render(request, 'core/index.html')

