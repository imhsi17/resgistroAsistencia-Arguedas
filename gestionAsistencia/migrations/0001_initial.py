# Generated by Django 4.2.4 on 2023-08-31 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('DNI', models.CharField(max_length=8)),
                ('contraseña', models.CharField(max_length=9)),
                ('grado', models.IntegerField()),
                ('seccion', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Atrasado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('fecha_ingreso', models.DateField()),
                ('hora_ingreso', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Puntual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('fecha_ingreso', models.DateField()),
                ('hora_ingreso', models.TimeField()),
            ],
        ),
    ]
