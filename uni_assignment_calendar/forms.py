from django import forms
from .models import Event

class IndexForm(forms.ModelForm):
    event_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Write a post...',
        }
    ))

    class Meta:
        model = Event
        fields = ('event_name', 'day', 'start_time', 'end_time', 'notes',)
