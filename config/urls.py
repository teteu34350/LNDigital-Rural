from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app import views

from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('animais/', AnimalListView.as_view(), name='lista_animais'),
    path('suino/', SuinoView.as_view(), name='suino'),
    path('animais/adicionar/', views.adicionar_animal, name='adicionar_animal')

]

