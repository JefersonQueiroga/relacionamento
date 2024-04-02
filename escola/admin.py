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

@admin.register(Cidade)
class CidadeAdmin( admin.ModelAdmin):
    list_display = ('nome', 'sigla_estado', 'cep', 'fundacao_cidade')
    search_fields = ['nome', 'sigla_estado']

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']   