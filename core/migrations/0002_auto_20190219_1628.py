# Generated by Django 2.1.7 on 2019-02-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueAdminForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entousai', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saida')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='obs',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='obs',
            name='entrada',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='obs',
            name='saida',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
