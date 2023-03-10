from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone

import datetime

from .forms import LoginForm, RegisterForm, AddAssignmentForm
from .models import Categories, Assignments


# Create your views here.


def index(request):
    assignments = Assignments.objects.filter(creator = request.user.id)
    now = timezone.now()
    for assignment in assignments.filter(missed=False):
        if assignment.due_time < now:
            assignment.missed = True
            assignment.save()
    categories = Categories.objects.filter(creator = request.user.id)
    add_assignment_form = AddAssignmentForm()
    return render(request, "manager/index.html", {
        "page":"assignments",
        "assignments":assignments,
        "now":now,
        "add_assignment_form":add_assignment_form,
        "categories":categories,})


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


def add_assignment(request):
    if request.method == "POST":
        form = AddAssignmentForm(request.POST)
        date = request.POST.get("date")
        time = request.POST.get("time")
        if form.is_valid:
            assignment = form.save(commit=False)
            return HttpResponse(assignment)
            if not assignment.category:
                new_category = Categories.objects.create(creator=request.user, category = request.POST.get("create_category"))
                return HttpResponse(new_category)
            assignment.creator = request.user
            due_date = request.POST["date"]
            due_time = request.POST["time"]
            assignment.due_time = datetime.datetime.strptime(f"{due_date} {due_time}:00", "%Y-%m-%d %H:%M:%S")
            assignment.save()
            return redirect("index")

        
    add_assignment_form = AddAssignmentForm()
    return render(request, "manager/add_assignment.html", {
        "page":"add",
        "add_assignment_form":add_assignment_form,
    })