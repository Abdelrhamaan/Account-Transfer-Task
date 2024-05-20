#!/bin/bash

# entrypoint.sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the PostgreSQL service to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

echo "PostgreSQL is up and running!"

# Apply database migrations
echo "Making and applying database migrations..."
python manage.py makemigrations
python manage.py migrate


# Create a superuser if it doesn't already exist
echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
username = '$DJANGO_SUPERUSER_USERNAME'
password = '$DJANGO_SUPERUSER_PASSWORD'
email = '$DJANGO_SUPERUSER_EMAIL'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
END


# Start the Django server
echo "Starting the Django server..."
exec python manage.py runserver 0.0.0.0:8000
