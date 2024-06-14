# Generated by Django 5.0.4 on 2024-06-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0010_alter_actor_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='apellido',
            field=models.CharField(max_length=75, verbose_name='Apellido de Actor'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='nombre',
            field=models.CharField(max_length=75, verbose_name='Nombre de Actor'),
        ),
        migrations.AlterField(
            model_name='director',
            name='apellido',
            field=models.CharField(max_length=75, verbose_name='Apellido de Director'),
        ),
        migrations.AlterField(
            model_name='director',
            name='nombre',
            field=models.CharField(max_length=75, verbose_name='Nombre de Director'),
        ),
    ]
