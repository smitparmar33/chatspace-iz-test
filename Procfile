web: gunicorn --bind :8000 --workers 3 --threads 2 spaceiz_chat.wsgi:application
websocket: daphne -b :: -p 5000 spaceiz_chat.asgi:application