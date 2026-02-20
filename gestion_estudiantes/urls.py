from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenido, name='bienvenido'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('estudiantesManejo/', views.listar_estudiantesManejo, name='listar_estudiantesManejo_manejo'),
    path('estudiantes/añadir/', views.anadir_estudianteManejo, name='anadir_estudiante_manejo'),
    path('estudiantes/eliminar/<str:estudiante_id>/', views.eliminar_estudianteManejo, name='eliminar_estudiante_manejo'),
    path('estudiantes/editar/<str:estudiante_id>/', views.editar_estudianteManejo, name='editar_estudiante_manejo')
]