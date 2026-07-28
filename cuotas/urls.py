from django.urls import path
from . import views


urlpatterns = [
    path('', views.cuotas, name='cuotas'),
    #Detalle pagar cuota (admin)
    path('detalle_pago/<int:id>/', views.detalle_pago_cuota, name='detalle_pago_cuota'),
    path('pagar_admin/<int:cuota_id>/',views.pagar_cuota_admin,name='pagar_cuota_admin'),
    # usuario sube comprobante
    path('subir_comprobante/<int:cuota_id>/', views.subir_comprobante, name='subir_comprobante'),
    #Comprobantes subidos, esperando ser aprobados o rechazados
    path('pagos_pendientes/', views.pagos_pendientes, name='pagos_pendientes'),
    #Aprobar pago
    path('pagos/aprobar/<int:pago_id>/', views.aprobar_pago, name='aprobar_pago'),
    #Rechazar Pago
    path('pagos/rechazar/<int:pago_id>/', views.rechazar_pago, name='rechazar_pago'),
    #Nuevo Plan
    path('plan/nuevo_plan', views.nuevo_plan, name='nuevo_plan'),
    path('plan/editar_plan/<int:id>', views.editar_plan, name='editar_plan'),
]
