## Django REST API
This is a sample application that shows how you can create a simple REST API using Django rest_framework.

# Prerequisites
To test the application. You need:
* Postman
* Django 1.11
* Python 3
* PostgreSQL
* psycopg2

# Usage
   * Clone [this](https://github.com/NewtonBii/django_rest_api) repository.
   * Navigate to the cloned directory and create a virtual environment ``python -m venv virtual``
   * Switch to the virtual environment ``source virtual/bin/activate``
   * Install all dependencies ``python -m pip install -r requirements.txt``
   * Create your own local database:
        * ``psql``
        * ``CREATE DATABASE <name of your database>``
  * Go to the ``settings.py`` module in the django_rest_api directory and change the databases configurations to point to the database
    you just created.

  * Migrate your models to your database: ``python manage.py makemigrations`` and then ``python manage.py migrate``

  * Launch the application using localhost server ``python manage.py runserver``
  * Now you can populate your database and make get requests to the server for example ``http://127.0.0.1:8000/api/users``
