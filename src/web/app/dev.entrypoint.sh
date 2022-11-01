#!/bin/sh

# uses the django-probes wait_for_database command
python manage.py wait_for_database

# run the migrations since not pushed to GitHub
# python manage.py makemigrations

# python manage.py flush --no-input
python manage.py migrate --no-input

# create admin superuser
python manage.py create_superuser --password secret


#populate db with test data
# python manage.py create_categories

# python manage.py create_user --username user --password secret

exec "$@"
