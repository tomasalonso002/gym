#!/bin/sh

echo "Esperando PostgreSQL..."

while ! nc -z "$DB_HOST" "$DB_PORT"; do
    sleep 1
done

echo "PostgreSQL listo"

echo "Aplicando migraciones..."
python manage.py migrate

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando Gunicorn..."
exec gunicorn gym.wsgi:application --workers 2 --bind 0.0.0.0:8000