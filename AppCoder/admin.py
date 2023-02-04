from django.contrib import admin

from AppCoder.forms import Programa, Tutor, Estudiante
from .models import*
from django.contrib import admin
from AppCoder.models import admin

class EstudianteAdmin(admin.TabularInline):
    model = Membership

class TutorAdmin(admin.ModelAdmin):
    inlines = [
        
    ]

class ProgramaAdmin(admin.ModelAdmin):
    inlines = [
        
    ]


class EstudianteAdmin(admin.ModelAdmin):
    inlines = ()
    
class TutorAdmin(admin.ModelAdmin):
    inlines = ()
    
class ProgramaAdmin(admin.ModelAdmin):
    inlines = ()



admin.site.register(Estudiante)
admin.site.register(Tutor)
admin.site.register(Programa)






