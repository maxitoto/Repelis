# Generated by Django 5.0.4 on 2024-04-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0002_actor_fotografia_director_fotografia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='director',
            field=models.ManyToManyField(to='fuente.director'),
        ),
    ]
