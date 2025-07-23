#!/usr/bin/env bash

echo "Running migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
gunicorn icode.wsgi:application
