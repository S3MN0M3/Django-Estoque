# Generated by Django 2.1.7 on 2019-02-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190219_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='entrada',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estoque',
            name='saida',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
