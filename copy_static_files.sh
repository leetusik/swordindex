#!/bin/bash

echo "Starting static files copy script..."

# Create the staticfiles directory if it doesn't exist
mkdir -p /app/staticfiles/img

# Check if there's a manifest file and remove it to force direct file serving
if [ -f /app/staticfiles/staticfiles.json ]; then
    echo "Found staticfiles.json manifest, removing it to bypass manifest issues..."
    rm -f /app/staticfiles/staticfiles.json
fi

# Check if the static/img directory exists
if [ -d /app/static/img ]; then
    echo "Found static/img directory, copying files..."
    
    # Copy all image files from static/img to staticfiles/img
    cp -rv /app/static/img/* /app/staticfiles/img/ || echo "Copy failed but continuing"
    
    # Set permissions
    chmod -R 755 /app/staticfiles
    find /app/staticfiles -type f -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.svg" 2>/dev/null | xargs -r chmod 644 || echo "No image files found for chmod"
    
    echo "Done copying static image files."
else
    echo "WARNING: /app/static/img directory not found!"
fi

# List the contents to verify
echo "Contents of staticfiles directory:"
find /app/staticfiles -type f | sort

# Create a symlink from static/img to staticfiles/img as a fallback
echo "Creating symlink from static/img to staticfiles/img as a fallback..."
ln -sf /app/static/img /app/staticfiles/img-link

echo "Static files copy script completed." 