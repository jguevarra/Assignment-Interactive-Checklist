release: python manage.py makemigrations
         python manage.py migrate
web: gunicorn cs3240_calendar.wsgi --log-file -