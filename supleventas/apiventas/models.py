
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Aqui se encuentra los modelos de clases

class Usuario(AbstractUser):
    ROLES = (
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='cliente')

    def __str__(self):
        return f"{self.username} - {self.rol}"

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="perfil")
    rut = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=15,blank=False, null=False)
    direccion = models.TextField(blank=False, null=False)
    gmail = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
@receiver(post_save, sender=Usuario)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=Usuario)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()


# Modelo de Categoría de Productos
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_categoria
    
# Modelo de Productos
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100,null=False)
    precio_producto = models.IntegerField(default=0,null=False)
    descripcion = models.TextField(default="",null=False)
    stock = models.IntegerField(default=10)
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto
