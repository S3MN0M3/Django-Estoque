# Generated by Django 2.1.7 on 2019-02-19 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190219_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='entousai',
            new_name='Entrada ou Saida',
        ),
        migrations.RemoveField(
            model_name='estoque',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='estoque',
            name='saida',
        ),
    ]
