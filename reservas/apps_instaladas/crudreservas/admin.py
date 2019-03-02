from django.contrib import admin
from apps_instaladas.crudreservas.models import UsuarioRol,Usuario,Medico,Disponibilidad_Agenda
# Register your models here.
admin.site.register(Usuario)
admin.site.register(UsuarioRol)
admin.site.register(Medico)
admin.site.register(Disponibilidad_Agenda)