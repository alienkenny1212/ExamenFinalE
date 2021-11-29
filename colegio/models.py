from django.db import models
from django.contrib import admin

# Create your models here.
class Alumno(models.Model):
    nombre_completo  =   models.CharField(max_length=30)
    carnet  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return self.nombre_completo

class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    descripcion =   models.CharField(max_length=100)
    ciclo      = models.IntegerField()
    alumnos   = models.ManyToManyField(Alumno, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)