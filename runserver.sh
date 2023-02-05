#!/bin/sh

./wait-for-it.sh

# Start the dev server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000