#!/bin/sh

sh ./docker-web-postgres.sh &
python manage.py collectstatic --no-input &&
python manage.py migrate &&
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='${DJANGO_ADMIN_USERNAME}').exists() or User.objects.create_superuser('${DJANGO_ADMIN_USERNAME}','${DJANGO_ADMIN_EMAIL}','${DJANGO_ADMIN_PASSWORD}');"
