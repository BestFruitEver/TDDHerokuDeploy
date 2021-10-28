#!/bin/sh

echo "Waiting for database..."

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "Database connected !"

exec "$@"
