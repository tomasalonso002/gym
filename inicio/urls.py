from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nueva_consulta/', views.nueva_consulta, name='nueva_consulta'),
    path('consultas/', views.get_consultas, name='get_consultas'),
    path('perfil/', views.perfil, name='perfil'),
    path('borrar_consulta/<int:id>', views.borrar_consulta, name='borrar_consulta')
]
