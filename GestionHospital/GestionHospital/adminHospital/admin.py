from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Doctor, Paciente, Enfermero, CitaMedica

admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Enfermero)
admin.site.register(CitaMedica)
