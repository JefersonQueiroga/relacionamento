from django.contrib import admin
from .models import Aluno, Cidade, Modalidade

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de alunos
    list_display = ('nome', 'email', 'cidade', 'ativo')
    # Permite filtrar os alunos por cidade
    list_filter = ('cidade', 'modalidades')
    # Adiciona uma caixa de pesquisa. A pesquisa será feita por nome e email do aluno
    search_fields = ['nome', 'email']
