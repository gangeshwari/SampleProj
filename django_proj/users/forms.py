from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Your name', max_length=100, help_text='')
    username = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']
