from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm
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