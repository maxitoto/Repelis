# Generated by Django 5.0.4 on 2024-06-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0012_alter_actor_apellido_alter_actor_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='critica',
            name='censura',
            field=models.BooleanField(default=False),
        ),
    ]
