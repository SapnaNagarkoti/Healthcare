# Healthcare
Healthcare Backend - Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/SapnaNagarkoti/Healthcare.git
cd Healthcare
2. Create and Activate a Virtual Environment
python -m venv env
env\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Database Configuration
Create a PostgreSQL database and a database user.

## settings.py

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost


5. Run Database Migrations
python manage.py makemigrations
python manage.py migrate
6. Run the Development Server
python manage.py runserver

## API Endpoints Overview
Authentication
Register:
POST /api/auth/register/
Body example:
json
{
  "username": "sapna",
  "email": "sapna@gmail.com",
  "password": "1234"
}
Login (JWT Token):
POST /api/auth/login/
Body example:

json
{
  "username": "sapna",
  "password": "1234"
}
Returns access and refresh JWT tokens.

Patient Management
POST /api/patients/ - Add new patient

GET /api/patients/ - List patients for the logged-in user

GET /api/patients/<id>/ - Get details of a patient

PUT /api/patients/<id>/ - Update patient details

DELETE /api/patients/<id>/ - Delete a patient

Doctor Management
POST /api/doctors/ - Add new doctor

GET /api/doctors/ - List all doctors

GET /api/doctors/<id>/ - Doctor details

PUT /api/doctors/<id>/ - Update doctor

DELETE /api/doctors/<id>/ - Delete a doctor

Patient-Doctor Mapping
POST /api/mappings/ - Assign doctor to patient

GET /api/mappings/ - List all mappings

GET /api/mappings/<patient_id>/ - List doctors assigned to a patient

DELETE /api/mappings/<id>/ - Remove a mapping
