from rest_framework.viewsets import ModelViewSet
from .models import Libro, Autor, Genero, Usuario
from .serializers import LibroSerializer, AutorSerializer, GeneroSerializer, UsuarioSerializer

# Create your views here.
class LibrosViewSet(ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = LibroSerializer

class AutoresViewSet(ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = AutorSerializer

class GeneroViewSet(ModelViewSet):
	queryset = Genero.objects.all()
	serializer_class = GeneroSerializer

class UsuarioViewSet(ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer