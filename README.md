# RESTful API using Django and Python to manage a list of books

This repository contains a simple Django CRUD API for managing a list of books. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on books. It was used appropriate HTTP methods for each endpoint (POST, GET, PUT, DELETE).

## Features

- Implemented using Django and Django REST Framework
- Provides endpoints for creating, retrieving, updating, and deleting books
- Includes appropriate status codes and error handling
- Ensures proper validation of input data

## Requirements

- [Django](https://www.djangoproject.com/): A high-level Python web framework.
- [Django REST Framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- [XAMPP](https://www.apachefriends.org/): It is a free and open-source cross-platform web server.
- [phpMyAdmin](https://www.phpmyadmin.net/): It is a free and open source administration tool for MySQL and MariaDB.
- [Visual Studio Code](https://code.visualstudio.com/download)

## Getting started

1. Clone the repository:

   ```bash
    https://github.com/Am-Issath/crud-django-rest-api.git
   ```
3. Connect XAMPP server
4. Create database with phpMyAdmin and name of the database **`book_db`**
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Change database configuration in the settings.py based on your requirement
7. Include the app(book) and rest_framwork in the settings.py under INSTALLED_APPS
8. Apply migrations:
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```
9. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Visit http://localhost:8000/api/book with your brower to access the application.



## Handling this web app

1. Visit http://localhost:8000/api/book with your browser and handle the list of books.
2. You can insert **ISBN**,**Title**,**Author**, **Publication date** and click the **`POST`** to check the HTTP status.
3. Visit http://localhost:8000/api/book/<id> based on the book id search.
4. With the **`Delete`** button you can delete the specific book tp check the HTTP status.
5. Or you can update the specific book details and click **`Put`** button then check the HTTP status.


