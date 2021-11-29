from django.contrib import admin
from colegio.models import Alumno, AlumnoAdmin, Curso, CursoAdmin
# Register your models here.
#Registramos nuestras clases principales.

admin.site.register(Curso, CursoAdmin)
admin.site.register(Alumno, AlumnoAdmin)