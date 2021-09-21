from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# トップページ用View
def top(request):
    return render(request, 'janken/top.html')