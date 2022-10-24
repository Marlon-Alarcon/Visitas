from django.contrib import admin
from apps.personas.models import Persona, Estudiante, Visitante

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pers_nombre', 'pers_apellido')

# Register your models here.
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Estudiante)
admin.site.register(Visitante)
