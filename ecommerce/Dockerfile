# syntax=docker/dockerfile:1
FROM python:alpine

LABEL maintainer='cybera.3s@gmail.com'
LABEL version='1.0.0'

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# django admin password
ENV DJANGO_SUPERUSER_PASSWORD admin

WORKDIR /app

COPY requirements.txt /app/

# upgrade pip
RUN pip install --upgrade pip
# install require packages
RUN pip3 install -r requirements.txt


COPY . /app/

# extract static files
RUN tar -xf static.tar.xz

EXPOSE 8000

CMD while ! python3 manage.py sqlflush > /dev/null 2>&1 ; do sleep 1; done && \
	python3 manage.py makemigrations --noinput && \
	python3 manage.py migrate --noinput && \
	python3 manage.py collectstatic --noinput && \
	python3 manage.py createsuperuser --phone 09150000000 --email admin@localhost --noinput; \
	gunicorn -b 0.0.0.0:8000 Ecommerce.wsgi
















