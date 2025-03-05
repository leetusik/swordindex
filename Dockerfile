FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    certbot \
    python3-certbot-nginx \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn psycopg2-binary

# Copy project files
COPY . .

# Add wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Add static files copy script
COPY copy_static_files.sh /app/copy_static_files.sh
RUN chmod +x /app/copy_static_files.sh

# Debug: List static directories before collectstatic
RUN echo "Contents of static directory:" && ls -la /app/static

# Make sure the staticfiles directory exists and is empty
RUN rm -rf /app/staticfiles && mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput --verbosity 2

# Debug: List collected files
RUN echo "Contents of staticfiles after collectstatic:" && ls -la /app/staticfiles

# Force copy image files regardless of collectstatic results
RUN mkdir -p /app/staticfiles/img && \
    if [ -d /app/static/img ]; then \
        echo "Copying image files from static/img to staticfiles/img" && \
        cp -rv /app/static/img/* /app/staticfiles/img/ || echo "Copy failed but continuing"; \
    else \
        echo "WARNING: /app/static/img directory not found!"; \
    fi

# Debug: List img directories
RUN echo "Contents of static/img:" && ls -la /app/static/img || echo "No static/img directory"
RUN echo "Contents of staticfiles/img:" && ls -la /app/staticfiles/img || echo "No staticfiles/img directory"

# Ensure proper permissions for static files
RUN chmod -R 755 /app/staticfiles
RUN find /app/staticfiles -type f -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.svg" 2>/dev/null | xargs -r chmod 644 || echo "No image files found for chmod"

# Configure nginx
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

EXPOSE 80 443

# Start nginx and gunicorn with additional static file copying
CMD /wait-for-it.sh db sh -c "/app/copy_static_files.sh && python manage.py migrate && service nginx start && gunicorn config.wsgi:application --bind 0.0.0.0:8000"