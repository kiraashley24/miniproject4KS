# miniproject4KS

INF 601 - Advanced Programming with Python -
Kira Selucky
-----

## Description
This project uses Django to run a web application. It is a ticketing form website for users to register accounts and log in.
Users are able to look through website but must be logged in to purchase tickets. 
-----

## Pip install instructions

Please run the following:

```
pip install -r requirements.txt
```



-----
## How to run this project
In a terminal window, please type the following:
```
python manage.py
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
``` 
-----
## Details on each command line
1. *python manage.py* - server environment, django-admin, sets DJANGO_SETTINGS_MODULE that points to project's settings.py 
2. *python manage.py migrate* - initializes database and creates tables
3. *python manage.py makemigrations* - applies changes to models
4. *python manage.py createsuperuser* - creates admin profile
5. *python manage.py runserver* - runs server to launch website
-----
## Web pages 

1. Home - index page, welcoming users
2. Food menu page - displays food options at theater
3. Showtimes page - shows what movies and times are currently showing
4. Tickets page - where registration/login appears, then shows purchase ticket form
5. Contact page