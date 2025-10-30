from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animais/', views.lista_animais, name='animais'),  # aqui mudou para lista_animais
    path('transacoes/', views.transacoes, name='transacoes'),
    path('lavouras/', views.lavouras, name='lavouras'),
    path('estoque/', views.estoque, name='estoque'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('veiculos/', views.veiculos, name='veiculos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pessoas/excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('animais/excluir/<int:id>/', views.excluir_animal, name='excluir_animal'),


]

