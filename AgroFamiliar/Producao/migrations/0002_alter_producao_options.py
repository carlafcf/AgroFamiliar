# Generated by Django 3.2.5 on 2022-02-14 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producao',
            options={'ordering': ['nome']},
        ),
    ]
