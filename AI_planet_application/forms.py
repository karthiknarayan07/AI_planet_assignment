from django import forms
from .models import Hackathon
from django.forms.widgets import DateTimeInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HackathonForm(forms.ModelForm):
    class Meta:
        model=Hackathon
        fields=['title','description','background_image','hackathon_image','submission_type','start_datetime','end_datetime','reward_prize']
        widgets = {
            'start_datetime': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime':DateTimeInput(attrs={'type': 'datetime-local'})
        }




class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']