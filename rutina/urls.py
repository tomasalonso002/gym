from django.urls import path
from . import views

urlpatterns = [
    path('', views.rutinas, name='rutinas'), 
    path('crear/', views.crear_rutina, name='crear_rutina'),
    path('crear_rutina_personalizada/<int:id>', views.crear_rutina_personalizada, name='crear_rutina_personalizada'),
    path('editar/<int:id>/', views.editar_rutina, name='editar_rutina'),
    path('<int:id>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),
    path('detalle_rutina/<int:id>', views.detalle_rutina,name='detalle_rutina')
]