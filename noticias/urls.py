from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('nueva_noticia/', views.nueva_noticia, name='nueva_noticia'),
    path('borrar_noticia/<int:id>/', views.borrar_noticia, name='borrar_noticia'), 
]