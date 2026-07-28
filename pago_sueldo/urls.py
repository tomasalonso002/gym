from django.urls import path
from . import views

urlpatterns = [
    path('carga_horaria/<int:id>/', views.carga_horaria, name='carga_horaria'),
    path('sueldo_hora/<int:id>/', views.sueldo_hora, name='sueldo_hora'),
]