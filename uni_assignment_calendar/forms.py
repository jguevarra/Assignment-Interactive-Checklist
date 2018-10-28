from django import forms
from .models import Events
import datetime

class IndexForm(forms.ModelForm):
    # event_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class':'form-control',
    #         'placeholder': 'Write a post...',
    #     }
    # ))
	due_date = forms.DateTimeField(input_formats=["%m/%d/%Y %H:%M"], widget=forms.DateTimeInput())   
	class Meta:
		model = Events
		exclude = ['pub_date']

