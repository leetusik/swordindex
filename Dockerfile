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

# Collect static files
RUN python manage.py collectstatic --noinput

# Ensure proper permissions for static files
RUN chmod -R 755 /app/staticfiles
RUN find /app/staticfiles/img -type f -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" -o -name "*.svg" | xargs ls -la

# Configure nginx
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

EXPOSE 80 443

# Start nginx and gunicorn
CMD /wait-for-it.sh db sh -c "python manage.py migrate && service nginx start && gunicorn config.wsgi:application --bind 0.0.0.0:8000"