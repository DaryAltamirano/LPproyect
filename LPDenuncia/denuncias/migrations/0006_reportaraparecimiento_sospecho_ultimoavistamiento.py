# Generated by Django 3.1.5 on 2021-01-25 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0005_auto_20210124_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='UltimoAvistamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescripcionLugar', models.TextField(max_length=200, verbose_name='Descripcion del lugar donde desaparecio')),
                ('Rango_Horario', models.TextField(max_length=200, verbose_name='Rango visto por ultima vez')),
                ('Ropa', models.TextField(max_length=200, verbose_name='Ropa del desaparecido')),
                ('Ubicacion', models.TextField(max_length=200, verbose_name='Ubicacion del avistamiento')),
                ('PersonaDesaparecida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.personadesaparecida')),
            ],
        ),
        migrations.CreateModel(
            name='Sospecho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apareiencia', models.TextField(max_length=200, verbose_name='Apariencia del sospechoso')),
                ('Motivo', models.TextField(max_length=200, verbose_name='Motivo de sospecha')),
                ('Sospecho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.personadesaparecida')),
            ],
        ),
        migrations.CreateModel(
            name='ReportarAparecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Condicion', models.TextField(max_length=200, verbose_name='Condicion de salud')),
                ('Ropa', models.TextField(max_length=200, verbose_name='Condicion de salud')),
                ('Fotografia', models.ImageField(blank=True, null=True, upload_to='Aparecidos/%Y/%m/%d')),
                ('PersonaDesaparecida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.personadenuncinate')),
            ],
        ),
    ]
