# Generated by Django 3.1.5 on 2021-01-25 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0004_personadesaparecida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personadesaparecida',
            name='PersonaDesaparecida',
        ),
        migrations.AddField(
            model_name='personadesaparecida',
            name='PersonaDesaparecida',
            field=models.ManyToManyField(to='denuncias.PersonaDenuncinate'),
        ),
    ]
