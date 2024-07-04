# Generated by Django 5.0.4 on 2024-06-19 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0005_alter_critica_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critica',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criticas', to='fuente.pelicula'),
        ),
    ]
