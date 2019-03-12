Starting a New Project

    django-admin startproject myproject

        myproject/                  <-- higher level folder
    |-- myproject/             <-- django project folder
    |    |-- myproject/
    |    |    |-- __init__.py
    |    |    |-- settings.py
    |    |    |-- urls.py
    |    |    |-- wsgi.py
    |    +-- manage.py
    +-- venv/                  <-- virtual environment folder

manage.py: 
    a shortcut to use the django-admin command-line utility. 
    It’s used to run management commands related to our project. 
    We will use it to run the development server, run tests, create migrations and much more.

__init__.py: 
    this empty file tells Python that this folder is a Python package.

settings.py: 
    this file contains all the project’s configuration. 
    We will refer to this file all the time!
urls.py: 
    this file is responsible for mapping the routes and paths in our project. 
    For example, if you want to show something in the URL /about/, you have to map it here first.
wsgi.py: 
    this file is a simple gateway interface used for deployment. 
    You don’t have to bother about it. Just let it be for now.


python manage.py runserver