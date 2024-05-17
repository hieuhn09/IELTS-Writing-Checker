from .models import UserWrittings
from django import forms

class WrittingForm(forms.ModelForm):
    class Meta:
        model = UserWrittings
        fields = ['task', 'writting']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'writting': forms.Textarea(),
        }