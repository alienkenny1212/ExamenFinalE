from django import forms
from .models import Curso, Alumno


class CursoForm(forms.ModelForm):
#todos los campos de curso
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion', 'ciclo', 'alumnos')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumnos"].help_text = "Seleccione a los alumnos que llevarán el curso"
        self.fields["alumnos"].queryset = Alumno.objects.all()

class AlumnoForm(forms.ModelForm):
    #todos los campos de curso
    class Meta:
        model = Alumno
        fields = ('nombre_completo', 'carnet', 'fecha_nacimiento', 'fecha_inscripcion')

    def __init__ (self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields["nombre_completo"].help_text = "Ingrese el nombre del alumno"
        self.fields["carnet"].help_text = "Ingrese el carnet del alumno"
        self.fields["fecha_nacimiento"].help_text = "Ingrese la fecha de nacimiento del alumno"
        self.fields["fecha_inscripcion"].help_text = "Ingrese la fecha de inscripción del alumno"

