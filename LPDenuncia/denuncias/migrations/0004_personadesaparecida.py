# Generated by Django 3.1.5 on 2021-01-25 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0003_auto_20210124_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaDesaparecida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=120, verbose_name='Nombre del desaparecido')),
                ('Appellido', models.TextField(max_length=200, verbose_name='Apellido del desaparecido')),
                ('Telefono', models.IntegerField()),
                ('TonoDePiel', models.CharField(max_length=120, verbose_name='Color de piel del desaparecido')),
                ('Edad', models.IntegerField()),
                ('ColorOjos', models.CharField(max_length=100, verbose_name='Color de los ojos')),
                ('Estatura', models.FloatField(max_length=4, verbose_name='Estatura del desapareido')),
                ('Fotografia', models.ImageField(blank=True, null=True, upload_to='Desaparecido/%Y/%m/%d')),
                ('PersonaDesaparecida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.personadenuncinate')),
            ],
        ),
    ]