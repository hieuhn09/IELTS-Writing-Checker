from .models import UserWrittings
from django import forms

class WrittingForm(forms.ModelForm):
    class Meta:
        model = UserWrittings
        fields = ['task', 'writting']
        widgets = {
            'task': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'writting': forms.Textarea(),
        }