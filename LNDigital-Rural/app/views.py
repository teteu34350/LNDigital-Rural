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



class FuncionarioListView(View):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionarios/lista.html', {'funcionarios': funcionarios})




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


def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, "animais/lista.html", {"animais": animais})

def remover_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    animal.delete()
    return redirect("lista_animais")  # redireciona de volta para a tabela