from django.db import models

class Especie(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Raca(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.especie.nome})"

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


