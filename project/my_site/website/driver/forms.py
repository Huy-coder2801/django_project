from django import forms
from django.contrib.auth.models import User
from website.models import Driver

class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class BasicDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('avatar', 'phone_number',)