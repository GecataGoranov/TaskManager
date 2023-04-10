from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView

import datetime

from .forms import LoginForm, RegisterForm, AddAssignmentForm
from .models import Categories, Assignments


# Create your views here.


def index(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    if request.method == "POST":


        if category_to_remove_str:=request.POST.get("category"):
            try:
                category_to_remove = Categories.objects.get(creator=request.user, category=category_to_remove_str)
                category_to_remove.delete()
            except:
                pass

        
        else:
            edited_assignment_content = request.POST.get("edit-assignment")
            return HttpResponse(edited_assignment_content)

    assignments = Assignments.objects.filter(creator = request.user.id, completed=False, category__category__icontains=q)
    now = timezone.now()
    for assignment in assignments.filter(missed=False):
        if assignment.due_time < now:
            assignment.missed = True
            assignment.save()
    categories = Categories.objects.filter(creator = request.user.id)
    add_assignment_form = AddAssignmentForm()
    
    for assignment in assignments:
        if not assignment.time_str:
            time = assignments.values_list("due_time__time", flat=True).get(id=assignment.id)
            assignment.time_str = time.strftime("%H:%M")
        if not assignment.date_str:
            date = assignments.values_list("due_time__date", flat=True).get(id=assignment.id)
            assignment.date_str = date.strftime("%m/%d/%Y")
        assignment.save()

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

        if form.is_valid():
            assignment = form.save(commit=False)
            try:
                if assignment.category:
                    pass
            except:
                new_category = Categories.objects.create(creator=request.user, category=request.POST.get("create_category"))
                new_category.save()
                assignment.category = new_category
            
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



class AddAssignmentCreateView(CreateView):
    model = Assignments
    form_class = AddAssignmentForm
    template_name = "manager/add_assignment.html"

    def form_valid(self, form):

        assignment = form.save(commit=False)

        if assignment.category:
            pass
        else:
            new_category = Categories.objects.create(creator=self.request.user, category=self.request.POST.get("category"))
            new_category.save()
            assignment.category = new_category

            assignment.creator = self.request.user

            due_date = self.request.POST.get("date")
            due_time = self.request.POST.get("time")
            assignment.due_time = datetime.datetime.strptime(f"{due_date} {due_time}:00", "%Y-%m-%d %H %M %S")
            
            assignment.save()

            return redirect(self.success_url)


class CompletedListView(ListView):
    template_name = "manager/completed.html"
    model = Assignments
    context_object_name = "assignments"

    def get_queryset(self):
        q = self.request.GET.get("q") if self.request.GET.get("q") is not None else ""
        return Assignments.objects.filter(creator=self.request.user.id, completed=True, category__category__icontains=q)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = "completed"
        context["categories"] = Categories.objects.filter(creator=self.request.user.id)
        return context

    def get(self, request, *args, **kwargs):
        pk = request.GET.get("pk")
        if pk:
            newly_completed_assignment = Assignments.objects.get(id=pk)
            newly_completed_assignment.completed = True
            newly_completed_assignment.save()     
        return super().get(request, *args, **kwargs)   

    def post(self, request):
        category_to_remove_str = request.POST.get("category")            
        category_to_remove = get_object_or_404(Categories, creator=request.user, category=category_to_remove_str)
        category_to_remove.delete()
        messages.success(request, f"Category {category_to_remove_str} was successfully removed.")
        context = self.get_context_data()
        return render(request, "manager/completed.html", context)