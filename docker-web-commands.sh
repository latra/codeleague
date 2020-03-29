#!/bin/sh

#sh ./docker-web-postgres.sh &&
python manage.py collectstatic --no-input &&
python manage.py migrate &&
gunicorn --bind 0.0.0.0:${DJANGO_PORT} codeleague.wsgi:application