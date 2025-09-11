from django.contrib import admin
from django.urls import path
from app import views  # importa views do app (ajuste "app" para o nome real do seu app!)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial
    path('', views.IndexView.as_view(), name='index'),

    # Listagem de animais
    path('animais/', views.AnimalListView.as_view(), name='animais'),

    # Suínos
    path('suino/', views.SuinoView.as_view(), name='suino'),
    path('suino/cadastrar/', views.cadastrar_suino, name='cadastrar_suino'),

    # Ações em animais
    path('animais/lista/', views.lista_animais, name='lista_animais'),
    path('animais/remover/<int:id>/', views.remover_animal, name='remover_animal'),
]
