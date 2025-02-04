# Online Book Store

A virtual bookstore where users can read and review books.

## Features

- User authentication (login, registration, and logout).
- Users can browse available books.
- Users can read book details and reviews.
- Submit and view book reviews.
- Admin panel for managing books, users, and orders.

# Installation
## 1- Clone the repository:
```
 git clone git@github.com:LouayTawfik/Online-Book-Store.git
 cd Online-Book-Store
```
## 2- Create a virtual environment:
```
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## 3- Install dependencies:
```
  cd src/
  pip install -r requirements.txt
```

## 4- Set up the database:
```
  Ensure PostgreSQL is installed and running.
  Update the DATABASE_URL in the .env file (see Environment Variables).
```
## 5- Run migrations:
```
  python manage.py migrate
```
## 6- Create a superuser (admin):
```
  python3 manage.py createsuperuser
```

## 7- Run the development server:
```
  python3 manage.py runserver
```
## 8- Access the application at http://127.0.0.1:8000/

# Environment Variables
### Create a .env file in the root directory and add the following variables:
```
 # .env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
```
* Replace your-secret-key with a secure secret key.
* Replace user, password, and dbname with your PostgreSQL credentials.

# Docker Setup
### To run the application using Docker:
## 1.Install Docker:
* Download and install Docker from https://www.docker.com/.
## 2.Build and run the containers:
```
 docker-compose up --build
```
## 3.Access the application at http://127.0.0.1:8000/.

# API Documentation:
The application uses Django REST Framework (DRF) for API endpoints. To view the API documentation:
## 1.Run the development server:
```
 python3 manage.py runserver
```
## 2.Access the API documentation at:
 * Swagger UI: http://127.0.0.1:8000/swagger/
 * ReDoc: http://127.0.0.1:8000/redoc/


