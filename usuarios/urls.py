from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_usuarios, name='get_usuarios'),
    path('empleados/', views.get_empleados, name='get_empleados'),
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('nuevo_empleado/', views.nuevo_empleado, name='nuevo_empleado'),
    path('borrar_usuario/<int:id>/', views.borrar_usuario, name='borrar_usuario'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
]