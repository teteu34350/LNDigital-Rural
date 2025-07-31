from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        # Inclui todos os campos do modelo no formulário.
        # Você pode especificar uma tupla de campos se não quiser todos:
        # fields = ['nome', 'especie', 'identificacao', 'data_nasc', 'genero', 'data_inseminacao', 'peso', 'raca']
        fields = '__all__'
        widgets = {
            # Adiciona um widget de data HTML5 para facilitar a seleção de datas
            'data_nasc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_inseminacao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # Adiciona classes Bootstrap para estilização dos campos
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'identificacao': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'raca': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Você pode adicionar validações ou personalizações adicionais aqui
    def clean_identificacao(self):
        identificacao = self.cleaned_data['identificacao']
        # Exemplo de validação: garantir que a identificação não seja muito curta
        if len(identificacao) < 3:
            raise forms.ValidationError("A identificação deve ter pelo menos 3 caracteres.")
        return identificacao
