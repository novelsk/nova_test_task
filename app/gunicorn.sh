python manage.py makemigrations &&
python manage.py migrate &&
gunicorn --certfile=./cert/YOURPUBLIC.pem --keyfile=./cert/YOURPRIVATE.key NOVA.wsgi:application --bind 0.0.0.0:443
