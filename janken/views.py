from janken.forms import GameForm, OpponentForm
from janken.models import Opponent, Game
from django.http.response import HttpResponse, HttpResponseForbidden

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

# トップページ用View
def top(request):
    user_id = request.user.id
    opponents = Opponent.objects.all()
    context = {
        'opponents': opponents
    }
    return render(request, 'janken/top.html', context)

@login_required
def opponent_detail(request, opponent_id):
    user_id = request.user.id
    opponent = get_object_or_404(Opponent, pk=opponent_id)
    form = GameForm()
    win_rate = round(Game.objects.filter(opponent=opponent_id).filter(result='勝ち').count() / Game.objects.filter(opponent=opponent_id).count() * 100, 1)
    if opponent.created_by.id == user_id:
        context = {
            'opponent': opponent,
            'form': form,
            'win_rate': win_rate,
        }
        return render(request, 'janken/opponent_detail.html', context)
    else:
        return HttpResponseForbidden('このページの閲覧は許可されていません')


@login_required
def opponent_new(request):
    if request.method == 'POST':
        form = OpponentForm(request.POST)
        if form.is_valid():
            opponent = form.save(commit=False)
            opponent.created_by = request.user
            opponent.save()
            return redirect('janken:top')
    else:
        form = OpponentForm()
        context = {
            'form': form
        }
        return render(request, 'janken/opponent_new.html', context)

@login_required
def game_register(request, opponent_id):
        if request.method == 'POST':
            form = GameForm(request.POST)
            if form.is_valid():
                game = form.save(commit=False)
                game.opponent_id = opponent_id
                game.created_by = request.user
                # 勝敗判定
                if int(game.my_hand) - int(game.opponent_hand) + 3 % 3 == 2:
                    game.result = '勝ち'
                elif int(game.my_hand) - int(game.opponent_hand) + 3 % 3 == 1:
                    game.result = '負け'
                else:
                    game.result = 'あいこ'
                game.save()
                return redirect('janken:op_detail', opponent_id)
        else:
            return HttpResponseForbidden('正規の手順を踏んでください')