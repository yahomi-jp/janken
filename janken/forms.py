from django import forms
from django.db import models
from django.db.models.base import Model
from .models import Opponent, Game

class OpponentForm(forms.ModelForm):
    class Meta:
        model = Opponent
        fields = ('name',)