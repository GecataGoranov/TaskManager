from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("register", views.registerPage, name="register"),
    path("add-assignment", views.AddAssignmentCreateView.as_view(), name="add"),
    path("completed", views.CompletedListView.as_view(), name="completed")
]