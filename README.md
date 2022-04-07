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
