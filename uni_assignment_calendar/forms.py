from django import forms
from .models import Events

class IndexForm(forms.ModelForm):
    event_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Write a post...',
        }
    ))

    class Meta:
        model = Events
        fields = ('class_abbrev', 'class_num', 'events_name', 'due_date', 'pub_date', 'description')
