from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PerfilViewSet, CategoriaViewSet, ProductosViewSet

# Configurar el router para la API
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfiles', PerfilViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductosViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto habilita todas las rutas definidas en el router
]
