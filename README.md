# django-blog
Blog with CMS system & very basic templates implemented in [Django Web Framework](https://www.djangoproject.com/).

## Requirements
- Django 2.0.7
- pytz 2018.5

## Installation
```bash
pip install -r requirements.txt
```

## Setup using Docker
```bash
docker-compose build
docker-compose run web python manage.py makemigrations posts users aboutme
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
```
