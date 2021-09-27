
from django.urls import path
from . import views

app_name = 'janken'

urlpatterns = [
    path('', views.top, name='top'),
    path('<int:opponent_id>/', views.opponent_detail, name='op_detail'),
    path('new/', views.opponent_new, name='op_new'),
    path('<int:opponent_id>/register/', views.game_register, name='game_register'),
]
