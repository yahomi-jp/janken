from janken.forms import OpponentForm
from janken.models import Opponent
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
    if opponent.created_by.id == user_id:
        context = {
            'opponent': opponent 
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