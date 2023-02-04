from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio,name='inicio'),
    #Estudiante
    path('estudiante',views.estudiante,name='estudiante'),
    path('formularioMEstudiante',views.formularioestudiante,name='formularioEstudiante'),
    path('leerEstudiante',views.leerEstudiante,name='leerEstudiante'),
    path('eliminarEstudiante/<estudiante_nombre>/',views.eliminarEstudiante,name='eliminarEstudiante'),
    path('editarEstudiante/<estudiante_nombre>/',views.editarEstudiante,name='editarEstudiante'),
    path('busquedaEstudiante',views.busquedaEstudiante,name='busquedaEstudiante'),
    path('buscar/',views.buscar),
    #Tutor
    path('tutor',views.tutor,name='Tutor'),
    path('formularioTutor',views.formularioTutor,name='formularioTutor'),
    path('leerTutor',views.leerTutor,name='leerTutor'), 
    path('eliminarTutor/<tutor_nombre>/',views.eliminarTutor,name='eliminarTutor'),
    path('editarTutor/<tutor_nombre>/',views.editarTutor,name='editarTutor'),

    #Programa
    path('programa',views.programa,name='programa'),
    path('formularioPrograma',views.formularioPrograma,name='formularioPrograma'),
    path('leerPrograma',views.leerPrograma,name='leerPrograma'), 
    path('eliminarTutor/<tutor_nombre>/',views.eliminarTutor,name='eliminarTutor'),
    path('editarTutor/<tutor_nombre>/',views.editarTutor,name='editarTutor'),


    #--------------Loguin/Register--------------------
    path('login',views.login_request, name='Login'),
    path('register',views.register, name='Register'),
    path('logout',LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
]