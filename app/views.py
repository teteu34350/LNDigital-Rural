from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Animal, Lavoura, Transacao, Veiculo, Estoque, Pessoa

# ---------- PÁGINAS PRINCIPAIS ----------
def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")
def login(request):
    return render(request, "login.html")

def transacoes(request):
    return render(request, 'transacoes.html')
def cadastro(request):
    return render(request, 'cadastro.html')

def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, "animais.html", {'animais': animais})

def lavouras(request):
    return render(request, 'lavouras.html')

def estoque(request):
    return render(request, 'estoque.html')

def pessoas(request):
    return render(request, 'pessoas.html')

def veiculos(request):
    return render(request, 'veiculos.html')


# ---------- ANIMAIS ----------
from django.shortcuts import render
from .models import Animal


from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def lista_animais(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animais')  # redireciona para a mesma página
    else:
        form = AnimalForm()

    animais = Animal.objects.all()
    total_animais = animais.count()
    bovinos = animais.filter(especie__iexact='Bovino').count()
    suinos = animais.filter(especie__iexact='Suíno').count()
    aves = animais.filter(especie__iexact='Ave').count()

    return render(request, 'animais.html', {
        'animais': animais,
        'total_animais': total_animais,
        'bovinos': bovinos,
        'suinos': suinos,
        'aves': aves,
        'form': form,
    })

def adicionar_animal(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        especie = request.POST.get('especie')
        raca = request.POST.get('raca')

        Animal.objects.create(
            nome=nome,
            especie=especie,
            raca=raca
        )
        return redirect('listar_animais')

    return render(request, 'animais/adicionar_animal.html')


# ---------- LAVOURAS ----------
def listar_lavouras(request):
    lavouras = Lavoura.objects.all()
    return render(request, 'lavouras/listar_lavouras.html', {'lavouras': lavouras})

def adicionar_lavoura(request):
    if request.method == 'POST':
        Lavoura.objects.create(
            nome=request.POST.get('nome'),
            tipo_cultura=request.POST.get('tipo_cultura'),
            area_hectares=request.POST.get('area_hectares'),
            data_plantio=request.POST.get('data_plantio'),
            data_colheita=request.POST.get('data_colheita'),
            produtividade_estimada=request.POST.get('produtividade_estimada'),
            observacoes=request.POST.get('observacoes')
        )
        return redirect('listar_lavouras')

    return render(request, 'lavouras/adicionar_lavoura.html')


# ---------- TRANSAÇÕES ----------
def listar_transacoes(request):
    transacoes = Transacao.objects.all().order_by('-data')
    return render(request, 'transacoes/listar_transacoes.html', {'transacoes': transacoes})
def transacoes(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        categoria = request.POST.get("categoria")
        tipo = request.POST.get("tipo")
        valor = request.POST.get("valor")
        data = request.POST.get("data")

        Transacao.objects.create(
            descricao=descricao,
            categoria=categoria,
            tipo=tipo.lower(),
            valor=valor,
            data=data
        )
        return redirect("transacoes")  # Redireciona para a mesma página

    todas_transacoes = Transacao.objects.all().order_by("-data")
    context = {
        "transacoes": todas_transacoes
    }
    return render(request, "transacoes.html", context)
# views.py
from django.shortcuts import render, redirect
from .models import Transacao  # <-- aqui sim você importa

def transacoes_view(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria', 'Outros')
        tipo = request.POST.get('tipo')
        valor = request.POST.get('valor')
        data = request.POST.get('data')

        Transacao.objects.create(
            descricao=descricao,
            categoria=categoria,
            tipo=tipo,
            valor=valor,
            data=data
        )
        return redirect('transacoes')

    transacoes = Transacao.objects.all().order_by('-data')
    return render(request, 'transacoes.html', {'transacoes': transacoes})

def adicionar_transacao(request):
    if request.method == 'POST':
        Transacao.objects.create(
            descricao=request.POST.get('descricao'),
            tipo=request.POST.get('tipo'),
            valor=request.POST.get('valor'),
            forma_pagamento=request.POST.get('forma_pagamento'),
            observacoes=request.POST.get('observacoes'),
            data=timezone.now()
        )
        return redirect('listar_transacoes')

    return render(request, 'transacoes/adicionar_transacao.html')


# ---------- VEÍCULOS ----------
def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/listar_veiculos.html', {'veiculos': veiculos})


def veiculos_view(request):
    veiculos = Veiculo.objects.all()  # Pega todos os veículos do banco
    return render(request, 'veiculos/veiculos.html', {'veiculos': veiculos})



def adicionar_veiculo(request):
    if request.method == 'POST':
        Veiculo.objects.create(
            placa=request.POST.get('placa'),
            modelo=request.POST.get('modelo'),
            marca=request.POST.get('marca'),
            ano=request.POST.get('ano'),
            tipo_combustivel=request.POST.get('tipo_combustivel'),
            km_atual=request.POST.get('km_atual'),
            status=request.POST.get('status'),
            observacoes=request.POST.get('observacoes')
        )
        return redirect('listar_veiculos')

    return render(request, 'veiculos/adicionar_veiculo.html')
from django.shortcuts import render, get_object_or_404
from .models import Veiculo  # Substitua pelo seu modelo real

from django.shortcuts import render
from .models import Veiculo

def veiculos_view(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/veiculos.html', {'veiculos': veiculos})



# ---------- ESTOQUE ----------
def listar_estoque(request):
    produtos = Estoque.objects.all()
    return render(request, 'estoque/listar_estoque.html', {'produtos': produtos})

def adicionar_estoque(request):
    if request.method == 'POST':
        Estoque.objects.create(
            produto=request.POST.get('produto'),
            quantidade=request.POST.get('quantidade'),
            unidade=request.POST.get('unidade'),
            valor_unitario=request.POST.get('valor_unitario'),
            observacoes=request.POST.get('observacoes')
        )
        return redirect('listar_estoque')

    return render(request, 'estoque/adicionar_estoque.html')


# ---------- PESSOAS ----------


from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa

def pessoas(request):
    if request.method == 'POST':
        pessoa_id = request.POST.get('pessoa_id')
        if pessoa_id:
            # edição
            pessoa = get_object_or_404(Pessoa, id=pessoa_id)
            pessoa.nome = request.POST.get('nome')
            pessoa.tipo = request.POST.get('tipo')
            pessoa.cpf = request.POST.get('cpf')
            pessoa.telefone = request.POST.get('telefone')
            pessoa.email = request.POST.get('email')
            pessoa.endereco = request.POST.get('endereco')
            pessoa.cidade = request.POST.get('cidade')
            pessoa.estado = request.POST.get('estado')
            pessoa.save()
        else:
            # criação
            Pessoa.objects.create(
                nome=request.POST.get('nome'),
                tipo=request.POST.get('tipo'),
                cpf=request.POST.get('cpf'),
                telefone=request.POST.get('telefone'),
                email=request.POST.get('email'),
                endereco=request.POST.get('endereco'),
                cidade=request.POST.get('cidade'),
                estado=request.POST.get('estado')
            )
        return redirect('pessoas')

    pessoas = Pessoa.objects.all()

    # Calcula os totais
    total_funcionarios = pessoas.filter(tipo="Funcionário").count()
    total_fornecedores = pessoas.filter(tipo="Fornecedor").count()
    total_clientes = pessoas.filter(tipo="Cliente").count()
    total_pessoas = pessoas.count()

    context = {
        'pessoas': pessoas,
        'total_funcionarios': total_funcionarios,
        'total_fornecedores': total_fornecedores,
        'total_clientes': total_clientes,
        'total_pessoas': total_pessoas,
    }

    return render(request, 'pessoas.html', context)

from django.shortcuts import redirect, get_object_or_404
from .models import Pessoa

def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoas')
    return redirect('pessoas')

from django.shortcuts import render, redirect
from .models import Animal

def animais(request):
    if request.method == 'POST':
        animal_id = request.POST.get('animal_id')

        nome = request.POST.get('nome')
        especie = request.POST.get('especie')
        idade = request.POST.get('idade')
        status = request.POST.get('status')

        if animal_id:
            # 🟡 Editar animal existente
            animal = get_object_or_404(Animal, id=animal_id)
            animal.nome = nome
            animal.especie = especie
            animal.idade = idade
            animal.status = status
            animal.save()
        else:
            # 🟢 Criar novo animal
            Animal.objects.create(
                nome=nome,
                especie=especie,
                idade=idade,
                status=status
            )

        return redirect('animais')

    # 🔵 Exibir lista
    animais = Animal.objects.all()
    total_animais = animais.count()

    return render(request, 'animais.html', {
        'animais': animais,
        'total_animais': total_animais
    })
def excluir_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    animal.delete()
    return redirect('animais')