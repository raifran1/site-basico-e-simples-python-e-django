# Generated by Django 2.2.4 on 2019-12-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_cliente_descricao_alunos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='mobilePhone',
            field=models.CharField(max_length=50),
        ),
    ]