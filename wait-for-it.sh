#!/bin/sh

# Wait for db to start
echo "Waiting for MongoDB to start..."
until nc -z db 27017; do
    sleep 1
done
echo "MongoDB has started."


echo "Waiting for SMTP to start..."
until nc -z smtp 25; do
    sleep 1
done
echo "Fake smtp server started."