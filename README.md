**Employer Management System (Django DRF)**

This is a simple Employer Management System built using  the Django REST Framework (DRF). It features custom user registration, login via JWT authentication, and basic CRUD operations for employer profiles.

**Features**

- User Signup (Registration)

- User Login using JWT (JSON Web Tokens)

- Profile View (Current User)

- Employers: Create, Read, Update, Delete (CRUD)

- Protected Endpoints (only accessible to authenticated users)

- User logout


**Technologies Used**

Python 3.13

Django 5.2

Django REST Framework (DRF)

Simple JWT (djangorestframework_simplejwt)

**Setup Instructions**

1. Create Virtual Environment

python -m venv env
env\Scripts\activate  (Windows)

2. Install Dependencies

pip install -r requirements.txt

3. Run Migrations

python manage.py makemigrations
python manage.py migrate

4. Run the Server

python manage.py runserver


**Authentication**

This project uses JWT for secure login.

On successful login, tokens are stored in the session.

Use the /api/auth/profile/ endpoint to view the logged-in user's profile.

**API Endpoints Summary**

| Method | Endpoint               | Description                     |
| ------ | ---------------------- | ------------------------------- |
| POST   |   /api/auth/signup/    | Register a new user             |
| POST   |  /api/auth/login/      | Login and get JWT tokens        |
| GET    |  /api/auth/profile/    | Get logged-in user's profile    |
| POST   |  /api/employers/       | Create a new Employer           |
| GET    |  /api/employers/       | List all Employers for the user |
| GET    |  /api/employers/<id>/  | Retrieve a specific Employer    |
| PUT    |  /api/employers/<id>/  | Update a specific Employer      |
| DELETE |  /api/employers/<id>/  | Delete a specific Employer      |


**Requirements**
Everything needed to run this project is listed in requirements.txt.


**Admin Access** (For Testing Purposes)

A Django superuser has been created to access the admin panel.

- Admin URL: http://127.0.0.1:8000/admin/
- Username: muskanahmed@gmail.com    
- Password: musk1234 


**Postman Collection** (For Testing)

To make testing easier, we’ve included a ready-to-use Postman collection.

-- [Download the Collection](./Employer_Management_System.postman_collection.json)

Once downloaded, you can import it into Postman:
1. Open Postman
2. Click on **Import**
3. Upload this JSON file
4. You'll see all the pre-configured requests ready to test



Feel free to ask questions or raise issues if something doesn't work as expected.

