from django import forms
from .models import MusicType, Music, Review
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Music
        fields='__all__'