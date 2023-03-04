from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
