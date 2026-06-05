from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_usuarios, name='get_usuarios'),
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('borrar_usuario/<int:id>/', views.borrar_usuario, name='borrar_usuario'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('register/', views.register, name='register'),

    #------- class ased views
    path("cbv/", views.get_usuarios.as_view()),
    path("cbv/nueva",views.nuevo_usuario.as_view()),
    path("cbv/editar/<int:pk>/", views.editar_usuario.as_view()),

]