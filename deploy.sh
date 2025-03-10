#!/bin/bash

echo "Starting deployment process..."

# Clean up Docker resources before rebuilding
echo "Cleaning up Docker resources..."
docker system prune -af --volumes
docker builder prune -af

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

# Storage management
echo "Performing storage management tasks..."

# Check disk usage
echo "Current disk usage:"
df -h /

# Remove old package cache
echo "Cleaning package cache..."
docker-compose exec web bash -c "apt-get clean || yum clean all || true"

# Final disk usage check
echo "Disk usage after cleanup:"
df -h /

echo "Deployment complete!"
echo "You can check the application logs with: docker-compose logs -f web"

# Storage management reminder
echo "-----------------------------------"
echo "STORAGE MANAGEMENT REMINDER:"
echo "If disk space is still low, consider:"
echo "1. Removing old backups: find /path/to/backups -name '*.bak' -mtime +30 -delete"
echo "2. Cleaning up more Docker resources: docker system prune -af --volumes"
echo "3. Increasing the EBS volume size if needed"
echo "-----------------------------------" 