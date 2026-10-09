from django.urls import path
from .views import InicioView, CursoView, EstudiantesView, ProfesoresView, EntregablesView
            #importamos las vistas
urlpatterns = [
    path('admin/', InicioView.as_view()),

    #vaciamos las rutas
                #seteamos como vista
    path('curso/', CursoView.as_view(),name='inicio'),
    path('estudiantes/', EstudiantesView.as_view(), name='estudiantes'),
    path('profesores/', ProfesoresView.as_view(),name='profesores'),
    path('entregables/', EntregablesView.as_view(), name='entregables'),

]
