# Generated by Django 5.0.3 on 2024-04-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_aluno_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='cep',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]
