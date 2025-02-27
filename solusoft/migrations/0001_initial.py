# Generated by Django 4.2.4 on 2023-12-03 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('estado_civil', models.CharField(choices=[('S', 'Soltero'), ('C', 'Casado'), ('V', 'Viudo'), ('D', 'Divorciado')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cargas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('parentesco', models.CharField(choices=[('C', 'Cónyuge'), ('H', 'Hijo/a')], max_length=1)),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solusoft.trabajador')),
            ],
        ),
    ]
