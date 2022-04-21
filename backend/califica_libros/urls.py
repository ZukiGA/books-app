from django.urls import path
from .views import LibrosViewSet, AutoresViewSet, GeneroViewSet, UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('libros', LibrosViewSet)
router.register('autores', AutoresViewSet)
router.register('genero', GeneroViewSet)
router.register('usuario', UsuarioViewSet)

urlpatterns = router.urls