python3 manage.py collectstatic --no-input
gunicorn codeleague.wsgi:application