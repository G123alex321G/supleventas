from rest_framework import serializers
from .models import Usuario, Perfil, Categoria, Productos

class PerfilSerializer(serializers.ModelSerializer):
    """Serializador del perfil, requiere rut, telefono, direccion y gmail obligatorios."""
    
    class Meta:
        model = Perfil
        fields = ['rut', 'telefono', 'direccion', 'gmail']

    def validate(self, data):
        """Validar que todos los campos sean obligatorios."""
        if not data.get('rut'):
            raise serializers.ValidationError({"rut": "Este campo es obligatorio."})
        if not data.get('telefono'):
            raise serializers.ValidationError({"telefono": "Este campo es obligatorio."})
        if not data.get('direccion'):
            raise serializers.ValidationError({"direccion": "Este campo es obligatorio."})
        if not data.get('gmail'):
            raise serializers.ValidationError({"gmail": "Este campo es obligatorio."})
        return data

class UsuarioSerializer(serializers.ModelSerializer):
    """Serializador de usuario, incluye el perfil como un campo anidado."""
    
    perfil = PerfilSerializer()  # Relación con Perfil

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'rol', 'perfil']
        extra_kwargs = {'password': {'write_only': True}}  # La contraseña solo se puede escribir

    def create(self, validated_data):
        """Crear usuario junto con su perfil."""
        perfil_data = validated_data.pop('perfil')  # Extraer los datos del perfil
        usuario = Usuario.objects.create_user(**validated_data)  # Crear el usuario
        Perfil.objects.create(usuario=usuario, **perfil_data)  # Crear el perfil con datos obligatorios
        return usuario

class CategoriaSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Categoria"""

    class Meta:
        model = Categoria
        fields = '__all__'
    
class ProductosSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Productos"""

    class Meta:
        model = Productos
        fields = '__all__'
