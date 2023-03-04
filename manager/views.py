from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import LoginForm
from .models import User
# Create your views here.


def index(request):
    return render(request, "manager/index.html")


def LoginPage(request):
    page = "login"
    form = LoginForm()
    return render(request, "manager/login_register.html", {"form":form})