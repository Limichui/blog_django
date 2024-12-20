# Generated by Django 5.1.3 on 2024-12-08 17:52

import curso.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("curso", "0004_alter_publicacion_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publicacion",
            name="duracion",
            field=models.IntegerField(
                help_text="Duración en minutos",
                validators=[curso.validators.validar_numeros_positivos],
            ),
        ),
        migrations.AlterField(
            model_name="publicacion",
            name="titulo",
            field=models.CharField(
                max_length=255, validators=[curso.validators.validar_longitud_minima]
            ),
        ),
    ]
