# forms.py
from django import forms
from .models import Suino

class SuinoForm(forms.ModelForm):
    class Meta:
        model = Suino
        fields = ['nome', 'identificacao', 'data_nascimento', 'peso'] 
