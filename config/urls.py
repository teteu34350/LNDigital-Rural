from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('animais/', AnimalListView.as_view(), name='animais'),
    path('suino/', SuinoView.as_view(), name='suino'),
    path('suino/cadastrar/', cadastrar_suino, name='suino'),
]