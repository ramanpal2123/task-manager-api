# Task Manager API

REST API with JWT Authentication and Role-Based Access

## Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## API Endpoints
- POST /api/v1/auth/register/ — Register
- POST /api/v1/auth/login/ — Login
- GET /api/v1/tasks/ — Get tasks
- POST /api/v1/tasks/ — Create task
- PUT /api/v1/tasks/{id}/ — Update task
- DELETE /api/v1/tasks/{id}/ — Delete task

## Swagger Docs
http://localhost:8000/swagger/

## Scalability Note
- Add Redis for caching frequent queries
- Use PostgreSQL for production
- Can be containerized with Docker
- Microservices ready structure

## Scalability Note
- Redis caching ke liye ready hai
- PostgreSQL production ke liye
- Docker containerization possible
- Microservices architecture support