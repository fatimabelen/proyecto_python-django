# Generated by Django 4.2.7 on 2023-12-01 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_clientes', '0001_initial'),
        ('app_coordinadores', '0001_initial'),
        ('app_servicios', '0001_initial'),
        ('app_empleados', '0002_alter_empleado_options'),
        ('app_reservas', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaservicio',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_clientes.cliente'),
        ),
        migrations.AddField(
            model_name='reservaservicio',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_empleados.empleado'),
        ),
        migrations.AddField(
            model_name='reservaservicio',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_coordinadores.coordinador'),
        ),
        migrations.AddField(
            model_name='reservaservicio',
            name='servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_servicios.servicio'),
        ),
    ]
