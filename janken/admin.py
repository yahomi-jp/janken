from janken.models import Opponent
from django.contrib import admin
from .models import Opponent, Game
# Register your models here.

admin.site.register(Opponent)
admin.site.register(Game)