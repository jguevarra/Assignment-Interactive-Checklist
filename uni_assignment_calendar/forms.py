from django import forms
from .models import Event

class IndexForm(forms.ModelForm):
    event_name = forms.CharField()

    class Meta:
        model = Event
        fields = ('event_name', 'day', 'start_time', 'end_time', 'notes',)
