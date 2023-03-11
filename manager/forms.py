from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Assignments, Categories


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control bg-secondary text-light",
                                                     "id":"username-login-input",
                                                     "placeholder":"Username"})
        self.fields["username"].label = "Username"

        self.fields["password"].widget.attrs.update({"class":"form-control bg-secondary text-light",
                                                     "id":"password-login-input",
                                                     "placeholder":"Password"})
        self.fields["password"].label = "Password"


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control bg-secondary text-light",
                                                     "id":"username-login-input",
                                                     "placeholder":"Username"})
        self.fields["username"].label = "Username"

        self.fields["password1"].widget.attrs.update({"class":"form-control bg-secondary text-light",
                                                     "id":"password-login-input",
                                                     "placeholder":"Password"})
        self.fields["password1"].label = "Password"
        
        self.fields["password2"].widget.attrs.update({"class":"form-control bg-secondary text-light",
                                                     "id":"password-login-input",
                                                     "placeholder":"Confirm Password"})
        self.fields["password2"].label = "Confirm Password"


class AddAssignmentForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="Add category", required=False)
    create_category = forms.CharField(required=False, widget=forms.TextInput(attrs={"id":"create-category",
                                                                "style":"display: none;",
                                                                "class":"form-control bg-secondary text-light mb-4",}))


    class Meta:
        model = Assignments
        fields = ["category", "create_category", "description"]
        ordering = ["category", "create_category"]

    def __init__(self, *args, **kwargs):
        super(AddAssignmentForm, self).__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({"class":"form-control bg-secondary text-light mb-1",
                                                     "id":"add-assignment-category",})
        self.fields["category"].label = "Add a category"

        self.fields["description"].widget.attrs.update({"class":"form-control bg-secondary mb-3 text-white",
                                                        "id":"add-assignment-description",
                                                        "style":"height: 200px;",})
        self.fields["description"].label = "Add a description"

