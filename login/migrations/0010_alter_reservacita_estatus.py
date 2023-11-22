# Generated by Django 4.2.4 on 2023-10-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_reservacita_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacita',
            name='estatus',
            field=models.CharField(choices=[('Agendada', 'agendada'), ('Cancelada', 'cancelada'), ('En espera de entrega de vehículo', 'en espera de entrega de vehículo'), ('En progreso', 'en progreso'), ('En espera de recogida de vehículo', 'en espera de recogida de vehículo'), ('Terminada', 'terminada')], default='Agendada', max_length=50),
        ),
    ]
