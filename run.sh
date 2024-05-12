lsof -t -i tcp:8000 | xargs kill -9
python manage.py runserver 0.0.0.0:8000
