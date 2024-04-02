from django.core.management.base import BaseCommand
from escola.models import Modalidade, Cidade, Aluno

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais para Modalidade, Cidade e Aluno'

    def handle(self, *args, **options):
        # Criando modalidades
        modalidades_nomes = ['Futebol', 'Vôlei', 'Natação', 'Atletismo']
        for nome in modalidades_nomes:
            Modalidade.objects.get_or_create(nome=nome)

        self.stdout.write(self.style.SUCCESS('Modalidades criadas com sucesso!'))

        # Criando cidades
        cidades_info = [
            ('São Paulo', 'SP'),
            ('Rio de Janeiro', 'RJ'),
            ('Belo Horizonte', 'MG'),
            ('Porto Alegre', 'RS')
        ]
        for nome, sigla_estado in cidades_info:
            Cidade.objects.get_or_create(nome=nome, sigla_estado=sigla_estado)

        self.stdout.write(self.style.SUCCESS('Cidades criadas com sucesso!'))

        # Criando alunos
        alunos_info = [
            ('João Silva', 'joao.silva@example.com', 'São Paulo', ['Futebol', 'Atletismo']),
            ('Maria Oliveira', 'maria.oliveira@example.com', 'Rio de Janeiro', ['Vôlei']),
            ('Carlos Pereira', 'carlos.pereira@example.com', 'Belo Horizonte', ['Natação', 'Futebol']),
        ]
        for nome, email, cidade_nome, modalidades_nomes in alunos_info:
            cidade = Cidade.objects.get(nome=cidade_nome)
            aluno, created = Aluno.objects.get_or_create(nome=nome, email=email, cidade=cidade)
            for modalidade_nome in modalidades_nomes:
                modalidade = Modalidade.objects.get(nome=modalidade_nome)
                aluno.modalidades.add(modalidade)
            aluno.save()

        self.stdout.write(self.style.SUCCESS('Alunos criados com sucesso!'))
