from django.contrib import admin
from .models import Autor, Genero, Libro, Usuario, Calificacion

# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Calificacion)
