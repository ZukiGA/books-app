Start

# Ejecutar servidor

npm run dev

# Crear ambiente virtual para backend

python -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject backend
cd backend
python manage.py runserver
python manage.py startapp califica_libros

# migrar tablas

python manage.py makemigrations
python manage.py sqlmigrate califica_libros 0001
python manage.py migrate

# crear usuario

python manage.py createsuperuser

# queries

python manage.py shell
from califica_libros.models import Autor, Genero, Libro, Usuario, Calificacion
autores = Autor.objects.all()
Libro.objects.raw('SELECT \* FROM califica_libros_libro')
