
from django.urls import path
from . import views

app_name = 'janken'

urlpatterns = [
    path('', views.top, name='top'),
]
