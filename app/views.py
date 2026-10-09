from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Curso
from .forms import CursoModelForm
class CursoCreateView(CreateView):
    model = Curso # Modelo objetivo
    form_class = CursoModelForm # El formulario inteligente asociado
    template_name = 'curso_form.html' # HTML a renderizar
    success_url = reverse_lazy('lista_cursos') # Redirección perezosa tras éxito
# Nota técnica: CreateView procesa los métodos GET, POST, la validación
# interna de datos y la invocación de .save() de manera automática.



# Create your views here.
class InicioView(View):
    def get(self, request):
        contexto=dict( #podemos pasarle variables a un html
            mensaje="Este es el inicio de tu App de Django", titulo="Home"

        )
        return render(request, "index.html", contexto)
                    #le pasamos el objeto request que espera un html
                                                     # la var es un diccionario
class CursoView(View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Cursos", titulo="Cursos", cursos=Curso.objects.all()#le pasamos (*)toda la tabla
        )
        return render(request,"index.html", contexto)


class ProfesoresView(View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Profesores", titulo="Profesores"
        )
        return render(request, "index.html", contexto)


    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
class EstudiantesView(View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Estudiantes", titulo="Estudiantes"
        )
        return render(request,"index.html", contexto)
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} | {self.email}"

class EntregablesView(View):
    def get(self, request):
        contexto = dict(  # podemos pasarle variables a un html
            mensaje="Vista de Entregables", titulo="Entregables"
        )
        return render(request,"index.html", contexto)
