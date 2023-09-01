from django.contrib import admin
from gestionAsistencia.models import Alumnos, Puntual, Atrasado

# Register your models here.
class Alumnos_admin(admin.ModelAdmin):
    
    list_display = ("nombre", "DNI")
    search_fields = ("nombre", "DNI")
    list_filter = ("grado", "seccion")

class Ingreso_admin(admin.ModelAdmin):
    
    list_display = ("DNI", "hora_ingreso")
    list_filter = ("fecha_ingreso",)
    date_hierarchy = "fecha_ingreso"


admin.site.register(Alumnos, Alumnos_admin)
admin.site.register(Puntual, Ingreso_admin)
admin.site.register(Atrasado, Ingreso_admin)