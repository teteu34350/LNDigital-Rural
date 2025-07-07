from django.db import models

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome:")
    data_nasc = models.DateField(verbose_name="Data de Nascimento:")
    CPF = models.CharField(max_length=11, unique=True, verbose_name="CPF:")
    telefone = models.CharField(max_length=20, verbose_name="Telefone:")
    email = models.CharField(max_length=70, verbose_name="Email:")

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    cargo = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    data_admissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    contato = models.CharField(max_length=100)
    endereco = models.TextField()
    status = models.CharField(max_length=20)
    historico_treinamentos = models.TextField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

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

class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    data_fabricacao = models.DateField(null=True, blank=True)
    validade = models.DateField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"


class Animal(models.Model):
    ESPECIE_OPC = [
        ('suíno','Suíno'),
        ('Suíno','Bovino'),
        ('Equino','Equino'),
        ('Aves','Aves'),
        ('Caprino','Caprino'),
        ('Coelho','Coelho')

    ]
    especie = models.CharField(max_length=50,choices = ESPECIE_OPC)
    nome = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=100)
    data_nasc = models.DateField()
    vacinacao = models.ForeignKey(Vacina, on_delete=models.SET_NULL, null=True)
    genero_opcoes = [
        ('M','Macho'),
        ('F','Fêmea')
    ]
    genero = models.CharField(max_length=10,choices = genero_opcoes)
    data_inseminacao = models.DateField(null=True, blank=True)
    peso = models.FloatField()
    raca_opcoes = [
        ('D','Duroc'),
        ('G','Gilt')
    ]
    raca = models.CharField(max_length=50,choices = raca_opcoes)
    def __str__(self):
        return f"{self.nome} - {self.identificacao}"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

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



class TransacaoFinanceira(models.Model):
    data = models.DateField(verbose_name="Data da Transação")
    tipo = models.CharField(max_length=50)
    descricao = models.TextField(max_length = 250)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=100)
    fornecedor_cliente = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.data} - {self.tipo} - {self.valor}"

    class Meta:
        verbose_name = "Finança"
        verbose_name_plural = "Finanças"

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

class Insumo(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    quantidade = models.FloatField()
    unidade_medida = models.CharField(max_length=20)
    data_aquisicao = models.DateField()
    validade = models.DateField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    local_armazenamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField()
    numero_serie = models.CharField(max_length=100)
    data_aquisicao = models.DateField()
    status = models.CharField(max_length=20)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

class ProdutoEstoque(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    quantidade = models.FloatField()
    tipo = models.CharField(max_length=50)
    unidade_medida = models.CharField(max_length=20)
    localizacao = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    lote = models.CharField(max_length=100)
    validade = models.DateField()
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
# Espécies de Animais
class Suino(models.Model):
    nome = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    peso = models.FloatField()

    def __str__(self):
        return f"{self.nome} - {self.identificacao}"
