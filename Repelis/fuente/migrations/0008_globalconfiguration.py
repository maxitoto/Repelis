# Generated by Django 5.0.4 on 2024-06-12 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuente', '0007_rename_tipo_categoria_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_action', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
