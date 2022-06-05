release: python manage.py migrate --noinput
web: gunicorn url_reduce.wsgi --log--file -heroku
web: gunicorn url_reduce.wsgi