from janken.models import Opponent
from django.http.response import HttpResponse, HttpResponseForbidden

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

# トップページ用View
def top(request):
    user_id = request.user.id
    opponents = Opponent.objects.filter(id=user_id)
    context = {
        'opponents': opponents
    }
    return render(request, 'janken/top.html', context)

@login_required
def opponent_detail(request, opponent_id):
    user_id = request.user.id
    opponent = get_object_or_404(Opponent, pk=opponent_id)
    if opponent.created_by.id == user_id:
        context = {
            'opponent': opponent 
        }
        return render(request, 'janken/opponent_detail.html', context)
    else:
        return HttpResponseForbidden('このページの閲覧は許可されていません')