# Generated by Django 3.2.5 on 2022-02-14 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producao', '0002_alter_producao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producao',
            options={'ordering': ['nome'], 'verbose_name': 'Produção', 'verbose_name_plural': 'Produções'},
        ),
    ]