from django import forms
from .models import FnB

class FnBForm(forms.ModelForm):
    class Meta:
        model = FnB
        fields = ('name', 'price', 'description', 'category')