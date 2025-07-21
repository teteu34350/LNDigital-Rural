from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class AnimalListView(View):
    def get(self, request):
        animais = Animal.objects.all()

        suinos_count = Animal.objects.filter(especie__icontains='su').count()
        bovinos_count = Animal.objects.filter(especie__icontains='bovi').count()
        equinos_count = Animal.objects.filter(especie__icontains='equin').count()
        caprinos_count = Animal.objects.filter(especie__icontains='caprin').count()

        print(f"Suinos: {suinos_count},Bovinos:{bovinos_count},Equinos:{equinos_count}")

        return render(request, 'animal.html', {
            'animais': animais,
            'suinos_count': suinos_count,
            'bovinos_count': bovinos_count,
            'equinos_count': equinos_count,
            'caprinos_count': caprinos_count,

        })
    
class SuinoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'suino.html')
    def post(self, request):
      pass
class UsuarioListView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


class LavouraListView(View):
    def get(self, request):
        lavouras = Lavoura.objects.all()
        return render(request, 'lavouras/lista.html', {'lavouras': lavouras})

class DoencaListView(View):
    def get(self, request):
        doencas = Doenca.objects.all()
        return render(request, 'doencas/lista.html', {'doencas': doencas})

class TransacaoFinanceiraListView(View):
    def get(self, request):
        transacoes = TransacaoFinanceira.objects.all()
        return render(request, 'financas/lista.html', {'transacoes': transacoes})

class FuncionarioListView(View):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionarios/lista.html', {'funcionarios': funcionarios})

class AtividadeListView(View):
    def get(self, request):
        atividades = Atividade.objects.all()
        return render(request, 'atividades/lista.html', {'atividades': atividades})

class VeiculoListView(View):
    def get(self, request):
        veiculos = Veiculo.objects.all()
        return render(request, 'veiculos/lista.html', {'veiculos': veiculos})

class InsumoListView(View):
    def get(self, request):
        insumos = Insumo.objects.all()
        return render(request, 'insumos/lista.html', {'insumos': insumos})

class EquipamentoListView(View):
    def get(self, request):
        equipamentos = Equipamento.objects.all()
        return render(request, 'equipamentos/lista.html', {'equipamentos': equipamentos})

class ProdutoEstoqueListView(View):
    def get(self, request):
        produtos = ProdutoEstoque.objects.all()
        return render(request, 'estoque/lista.html', {'produtos': produtos})

class FornecedorListView(View):
    def get(self, request):
        fornecedores = Fornecedor.objects.all()
        return render(request, 'fornecedores/lista.html', {'fornecedores': fornecedores})

class VacinaListView(View):
    def get(self, request):
        vacinas = Vacina.objects.all()
        return render(request, 'vacinas/lista.html', {'vacinas': vacinas})
# Views para adicionar animais 
def cadastrar_suino(request):
    if request.method == 'POST':
        form = SuinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suino')  
    else:
        form = SuinoForm()
    
    return render(request, 'suino.html', {'form': form})


