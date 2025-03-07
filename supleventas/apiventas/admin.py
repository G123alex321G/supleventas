from django.contrib import admin
from .models import Usuario, Perfil, Categoria, Productos

# Registro de modelos en el panel de administración
admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Productos)