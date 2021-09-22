from janken.models import Opponent
from django.http.response import HttpResponse

from django.shortcuts import render, get_object_or_404

# Create your views here.

# トップページ用View
def top(request):
    return render(request, 'janken/top.html')


def opponent_detail(request, opponent_id):
    opponent = get_object_or_404(Opponent, pk=opponent_id)
    context = {
        'opponent': opponent
    }
    return render(request, 'janken/opponent_detail.html', context)