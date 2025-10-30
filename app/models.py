from django.db import models

# ===================== ANIMAIS =====================
class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.CharField(max_length=20, blank=True, null=True)
    STATUS_CHOICES = [
        ("saudavel", "Saudável"),
        ("observacao", "Em observação"),
        ("tratamento", "Em tratamento"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="saudavel")

    def __str__(self):
        return self.nome

# ===================== LAVOURAS =====================
class Lavoura(models.Model):
    nome = models.CharField(max_length=100)
    tipo_cultura = models.CharField(max_length=100)
    area_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    data_plantio = models.DateField()
    data_colheita = models.DateField(null=True, blank=True)
    produtividade_estimada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo_cultura})"

# ===================== TRANSACOES =====================
class Transacao(models.Model):
    TIPO_CHOICES = [
        ("receita", "Receita"),
        ("despesa", "Despesa"),
    ]

    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, default='Outros')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - {self.tipo} - {self.valor}"

# ===================== VEICULOS =====================
class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    tipo_combustivel = models.CharField(max_length=50, blank=True, null=True)
    km_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50, default='Disponível')
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

# ===================== ESTOQUE =====================
class Estoque(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=0)
    unidade = models.CharField(max_length=20, default='un')
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_entrada = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.produto} ({self.quantidade} {self.unidade})"

# ===================== PESSOAS =====================
from django.db import models

class Pessoa(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    TIPO_CHOICES = [
        ('Funcionário', 'Funcionário'),
        ('Fornecedor', 'Fornecedor'),
        ('Cliente', 'Cliente'),
    ]

    nome = models.CharField("Nome Completo", max_length=100)
    data_nascimento = models.DateField("Data de Nascimento", blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    cargo = models.CharField("Cargo", max_length=50, blank=True, null=True)
    endereco = models.TextField("Endereço", blank=True, null=True)
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default='ativo')
    historico_treinamentos = models.TextField("Histórico de Treinamentos", blank=True, null=True)
    observacoes = models.TextField("Observações", blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True, null=True)
    data_cadastro = models.DateField("Data de Cadastro", auto_now_add=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)



    def __str__(self):
        return self.nome

