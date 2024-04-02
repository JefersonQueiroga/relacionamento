from django.db import models

class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    sigla_estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    fundacao_cidade = models.DateField()

    def __str__(self):
        return self.nome

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    modalidades=models.ManyToManyField(Modalidade)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    