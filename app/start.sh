python manage.py makemigrations &&
python manage.py migrate &&
uvicorn NOVA.asgi:application --host 0.0.0.0 --port 443 --ssl-certfile ./cert/YOURPUBLIC.pem --ssl-keyfile ./cert/YOURPRIVATE.key &
celery -A NOVA worker --loglevel=INFO
