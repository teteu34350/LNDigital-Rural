from django.db import models

# -------------------- ESPÉCIES E RAÇAS --------------------
class Especie(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Raca(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name="racas")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.especie.nome})"


# -------------------- ANIMAIS --------------------
class Animal(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name="Espécie")
    raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Raça")
    nome = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=100, unique=True)
    data_nasc = models.DateField()
    genero_opcoes = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    genero = models.CharField(max_length=1, choices=genero_opcoes)
    data_inseminacao = models.DateField(null=True, blank=True)
    peso = models.FloatField()

    def __str__(self):
        return f"{self.nome} - {self.identificacao}"


# -------------------- USUÁRIOS --------------------
class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    CPF = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.CharField(max_length=70, verbose_name="Email")

    def __str__(self):
        return self.nome


# -------------------- UNIDADES DE MEDIDA --------------------
class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50, unique=True)  # ex: "kg", "litro", "unidade"

    def __str__(self):
        return self.nome


# -------------------- CARGOS --------------------
class Cargo(models.Model):
    nome = models.CharField(max_length=50, unique=True)  # ex: "Gerente", "Agrônomo"

    def __str__(self):
        return self.nome


# -------------------- FUNCIONÁRIOS --------------------
class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)  # Link com Cargo
    departamento = models.CharField(max_length=50)
    data_admissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    contato = models.CharField(max_length=100)
    endereco = models.TextField()
    status = models.CharField(max_length=20)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"


# -------------------- LAVOURAS --------------------
class Lavoura(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    cultura = models.CharField(max_length=100)
    variedade = models.CharField(max_length=100)
    data_plantio = models.DateField()
    data_previsa = models.DateField()
    adubacoes = models.TextField()
    irrigacao = models.TextField()
    responsaveis = models.ManyToManyField(Funcionario)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Lavoura"
        verbose_name_plural = "Lavouras"


# -------------------- DOENÇAS --------------------
class Doenca(models.Model):
    nome = models.CharField(max_length=100)
    sintomas = models.TextField()
    data_inicio = models.DateField()
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"


# -------------------- ATIVIDADES --------------------
class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    materiais_necessarios = models.TextField()
    funcionario_responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_registro = models.DateField()
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"


# -------------------- TRANSAÇÕES FINANCEIRAS --------------------
class TransacaoFinanceira(models.Model):
    data = models.DateField(verbose_name="Data da Transação")
    tipo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=100)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.data} - {self.tipo} - {self.valor}"

    class Meta:
        verbose_name = "Finança"
        verbose_name_plural = "Finanças"


# -------------------- VEÍCULOS --------------------
class Veiculo(models.Model):
    tipo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField()
    capacidade_carga = models.FloatField()
    status = models.CharField(max_length=20)
    historico_manutencao = models.TextField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.placa}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"


# -------------------- CATEGORIAS --------------------
class Categorias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
