from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Perfil, Categoria, Productos
from .serializers import UsuarioSerializer, PerfilSerializer, CategoriaSerializer, ProductosSerializer
# Create your views here.



# Vista para gestionar Usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para gestionar Perfiles
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

# Vista para gestionar Categorías
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vista para gestionar Productos
class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
