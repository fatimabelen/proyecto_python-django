# Generated by Django 4.2.7 on 2023-12-09 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clientes', '0002_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['id']},
        ),
    ]