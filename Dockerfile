# Use official Python runtime as base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy all project files
COPY . /app/

# Create startup script
RUN echo '#!/bin/sh\n\
set -e\n\
echo "Running migrations..."\n\
python manage.py migrate --noinput\n\
echo "Collecting static files..."\n\
python manage.py collectstatic --noinput\n\
echo "Starting Gunicorn..."\n\
exec gunicorn lawforyou.wsgi:application --bind 0.0.0.0:8000 --workers 4' > /app/start.sh && \
chmod +x /app/start.sh

# Open port
EXPOSE 8000

# Run startup script
CMD ["/app/start.sh"]
