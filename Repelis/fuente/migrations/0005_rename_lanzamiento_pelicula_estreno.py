# Generated by Django 5.0.4 on 2024-06-11 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0004_alter_actor_fotografia_alter_director_fotografia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='lanzamiento',
            new_name='estreno',
        ),
    ]
