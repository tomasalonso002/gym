from django.contrib import admin
from .models import Plan, Cuota, Pago

# Register your models here.

admin.site.register(Plan)
admin.site.register(Cuota)
admin.site.register(Pago)