from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    correo = models.EmailField()
    contrasena = models.CharField(max_length=100)
    def __str__(self):
        return self.correo

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    portada = models.FileField()
    fecha_publicacion = models.DateField()
    num_pag = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor) 
    calificaciones = models.ManyToManyField(Usuario, through='Calificacion')


    def __str__(self):
        return self.titulo


class Calificacion(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.DecimalField(decimal_places=2, max_digits=4)
    comentario = models.TextField()

    def __str__(self):
        return str(self.calificacion) + "-" + self.comentario