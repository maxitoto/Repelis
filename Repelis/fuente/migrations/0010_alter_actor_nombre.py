# Generated by Django 5.0.4 on 2024-06-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0009_delete_globalconfiguration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nombre',
            field=models.CharField(max_length=75, verbose_name='Actor'),
        ),
    ]