from django import forms
from .models import Assignment

class IndexForm(forms.ModelForm):
    event_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Write a post...',
        }
    ))

    class Meta:
        model = Assignment
        fields = ('assignment_name', 'due_date', 'pub_date', 'description')
