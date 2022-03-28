from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=100)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    data_publi = models.DateField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
