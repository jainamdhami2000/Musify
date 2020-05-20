from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class MusicLinkForm(forms.ModelForm):

    class Meta:
        model = MusicLink
        fields = ['link']

class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        exclude = ['slug','image']
        widgets = {
            'year_of_release': DateInput()
        }

class MusicForm2(forms.ModelForm):

    class Meta:
        model = Music
        exclude = ['slug']
        widgets = {
            'year_of_release': DateInput()
        }

class MusicLinkForm(forms.ModelForm):

    class Meta:
        model = MusicLink
        fields = ['link']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
