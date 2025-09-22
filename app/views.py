from django.shortcuts import render
from .models import Animal  # só se quiser usar a tabela

def index(request):
    return render(request, "index.html")  # página inicial


def lista_animais(request):
    return render(request, "animais.html")  # renderiza o template animal.html

def transacoes(request):
    return render(request, 'transacoes.html')

def animais(request):
    return render(request, 'animais.html')

def lavouras(request):
    return render(request, 'lavouras.html')

def estoque(request):
    return render(request, 'estoque.html')

def pessoas(request):
    return render(request, 'pessoas.html')

def veiculos(request):
    return render(request, 'veiculos.html')

def index(request):
    return render(request, 'index.html')

