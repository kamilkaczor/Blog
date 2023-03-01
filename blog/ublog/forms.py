from django import forms
from .models import BlogEntryModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(widget=forms.PasswordInput, max_length=63)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BlogEntryForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Type text ...',
                                                                               'rows': 5,
                                                                               'cols': 100,
                                                                               }), label='',)

    class Meta:
        model = BlogEntryModel
        fields = ['body']
