# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set environment variables for superuser creation
ENV DJANGO_SU_NAME admin
ENV DJANGO_SU_EMAIL admin@example.com
ENV DJANGO_SU_PASSWORD password

# Set work directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy project
COPY ./mysite /app/


# CMD will run when the container is launched
CMD python mysite/scripts/create_superuser.py && gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
#CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]


