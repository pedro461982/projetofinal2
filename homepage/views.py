from django.shortcuts import render
from produtos.models import Produto

def homepage(request):
    produtos = Produto.objects.all()  # Carrega todos os produtos
    return render(request, 'home.html', {'produtos': produtos})
