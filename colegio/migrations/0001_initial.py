# Generated by Django 2.2.24 on 2021-11-29 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=30)),
                ('carnet', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_inscripcion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=100)),
                ('ciclo', models.IntegerField()),
                ('alumnos', models.ManyToManyField(through='colegio.Asignacion', to='colegio.Alumno')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Curso'),
        ),
    ]
