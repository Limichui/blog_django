# Generated by Django 5.1.3 on 2024-12-06 01:22

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_alter_publicacion_imagen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='duracion',
            field=models.IntegerField(help_text='Duración en minutos', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.publicacion')),
            ],
            options={
                'unique_together': {('publicacion', 'autor')},
            },
        ),
    ]