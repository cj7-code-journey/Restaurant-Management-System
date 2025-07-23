#!/bin/bash

# Exit on error
set -e

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn icode.wsgi:application --bind 0.0.0.0:$PORT
