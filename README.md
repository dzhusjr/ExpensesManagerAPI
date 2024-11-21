# Task Manager Project

## Overview
This is a Expenses Manager project built with Python and Django REST framework. It allows users to manage expenses and user accounts, with the following features:
- API to create, update, view, and delete users and their expenses.
- Assign expenses to users, with constraints.
- View expenses by category or date range, including pagination.
- View summary of expenses by each category.

## Requirements
- Python 3+
- Docker & Docker Compose
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/dzhusjr/TaskManagerAPI.git
cd TaskManagerAPI
```
Create a `.env` file in the root directory with the following content:

```
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DB=<your_postgres_db>
SECRET_KEY=<your_django_secret_key>
```
Or copy the contents of .env.example into your .env for a test run.

### 2. Set Up Docker
Make sure Docker is installed and running. Run the following command to build and run the containers:

```bash
docker-compose up --build -d
```

This will:
- Set up a PostgreSQL database.
- Set up the Django application server using Gunicorn.

### 3. Run Migrations
After the containers are up and running, run the database migrations:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### 4. Access the Application
- The API should be available at `http://localhost:8000/`.
- Use tools like Postman or cURL to interact with the API.

## API Endpoints
### User Management
- **List Users**: `GET /api/users/`
- **Retrieve User**: `GET /api/users/{id}/`
- **Delete User**: `DELETE /api/users/{id}/` (requires password)
- **Create User**: `POST /api/users/`
- **Update User**: `PATCH /api/users/{id}/` (partial update)

### Expenses Management
- **List Expenses**: `GET /api/expenses/`
- **Retrieve Expense**: `GET /api/expenses/{id}/`
- **Delete Expense**: `DELETE /api/expenses/{id}/`
- **Create Expense**: `POST /api/expenses/`
- **Update Expense**: `PATCH /api/expenses/{id}/` (partial update)
- **View Expenses by Category**: `GET /api/expenses/by_category/?category={category}`
- **View Expenses by Date Range**: `GET /api/expenses/category_summary/?user_id=1&month=11`
- **View Summary by Category**: `GET /api/expenses/category_summary/?user_id=1&&month=11`

## Notes
- The project uses **Docker** for containerization.
- The project follows **PEP-8** standards.
- Ensure all sensitive data is managed through the `.env` file.
