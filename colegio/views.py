from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm, AlumnoForm
from colegio.models import Asignacion, Curso, Alumno
# Create your views here.

def curso_nuevo(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'], ciclo = formulario.cleaned_data['ciclo'])
            for alumno_id in request.POST.getlist('alumnos'):
                asignacion = Asignacion(alumno_id=alumno_id, curso_id = curso.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso creado exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'colegio/curso_editar.html', {'formulario': formulario})

def alumno_nuevo(request):
    if request.method == "POST":
        formulario = AlumnoForm(request.POST)
        if formulario.is_valid():
            alumno = Alumno.objects.create(nombre_completo=formulario.cleaned_data['nombre_completo'], carnet = formulario.cleaned_data['carnet'], fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento'], fecha_inscripcion = formulario.cleaned_data['fecha_inscripcion'])
            messages.add_message(request, messages.SUCCESS, 'alumno creado exitosamente')
    else:
        formulario = AlumnoForm()
    return render(request, 'colegio/alumno_editar.html', {'formulario': formulario})