#!/bin/bash

echo "Starting deployment process..."

# Rebuild the Docker containers with the new configuration
echo "Rebuilding Docker containers..."
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Wait for containers to start
echo "Waiting for containers to start..."
sleep 10

# Check if the containers are running
echo "Checking container status..."
docker-compose ps

# Run collectstatic to ensure all static files are collected
echo "Collecting static files..."
docker-compose exec web python manage.py collectstatic --noinput

# Check Nginx logs for any errors
echo "Checking Nginx logs for errors..."
docker-compose exec web bash -c "tail -n 50 /var/log/nginx/error.log"

echo "Deployment complete!"
echo "You can check the application logs with: docker-compose logs -f web" 