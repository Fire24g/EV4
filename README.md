
# Mantención Industrial API (Django + DRF)

API RESTful para gestionar empresas, equipos, técnicos, planes de mantención y órdenes de trabajo.
Respuestas en JSON y autenticación JWT. Lectura pública; escritura para usuarios autenticados.

## Requisitos
- Python 3.10+
- Django
- djangorestframework
- djangorestframework-simplejwt

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
