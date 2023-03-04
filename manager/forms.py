from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control bg-secondary",
                                                     "id":"username-login-input",
                                                     "placeholder":"Username"})
        self.fields["username"].label = "Username"
        self.fields["password"].widget.attrs.update({"class":"form-control bg-secondary",
                                                     "id":"password-login-input",
                                                     "placeholder":"Password"})
        self.fields["password"].label = "Password"


