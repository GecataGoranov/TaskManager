from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


from .forms import LoginForm, RegisterForm


# Create your views here.


def index(request):
    return render(request, "manager/index.html", {"page":"assignments"})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist.")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Username and password do not match.")

        
    
    login_form = LoginForm()
    return render(request, "manager/login_register.html", {
        "page":"login",
        "login_form":login_form})
    

def logoutPage(request):
    logout(request)
    return redirect("index")


def registerPage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except(ValueError):
                messages.error(request, "Invalid password.")
                messages.error(request, "Your password can't be too similar to your other personal information.")
                messages.error(request, "Your password must contain at least 8 characters.")
                messages.error(request, "Your password can't be a commonly used password.")
                messages.error(request, "Your password can't be entirely numeric")
        else:
            messages.error(request, "Passwords don't match.")


    register_form = RegisterForm()
    return render(request, "manager/login_register.html", {
        "page":"register",
        "register_form":register_form
    })