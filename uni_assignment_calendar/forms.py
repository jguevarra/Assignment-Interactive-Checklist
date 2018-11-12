from django import forms
from .models import Events
from django.contrib.auth.models import User
import datetime

class IndexForm(forms.ModelForm):
    due_date = forms.DateField(input_formats=["%m/%d/%Y"], widget=forms.DateInput(format=["%m/%d/%Y"]))
    due_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    class Meta:
	    model = Events
	    exclude = ['pub_date']


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password')
