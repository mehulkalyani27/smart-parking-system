from email.parser import FeedParser
from django import forms
from .models import feedback

class Formfeedback(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ["name","contact","email","pstorey","feedback"]