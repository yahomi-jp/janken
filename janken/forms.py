from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields
from .models import Opponent, Game

class OpponentForm(forms.ModelForm):
    class Meta:
        model = Opponent
        fields = ('name',)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('opponent_hand', 'my_hand')