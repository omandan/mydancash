from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Email,Account
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class EmailAddForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['value','vsbilty']


class UserEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


class PersonalEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['image']