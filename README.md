# Public API - Retrieve Basic Information
This is a simple Django-based public API that returns basic information in JSON format. The API provides:
•	Your registered email address
•	The current datetime in ISO 8601 format (UTC)
•	The GitHub URL of the project's codebase

# API Endpoint
Base URL: https://https://hng12stage0-3.onrender.com
GET /api/
Response Format (200 OK)
{
  "email": "inyelegoody@gmail.com",
  "current_datetime": "2025-02-02T09:30:00Z",
  "github_url": "https://github.com/ginyele/hng12stage0.git"
}

# Installation and Setup
Prerequisites
•	Python 3.x
•	Django
•	Git
•	A Render account for deployment

# Local Setup
1.	Clone the repository:
2.	git clone https://github.com/ginyele/hng12stage0.git
cd hng12stage0
3.	Create a virtual environment and activate it:
4.	python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
5.	Install dependencies:
pip install -r requirements.txt
6.	Run the server:
python manage.py runserver
The API will be available at http://127.0.0.1:8000/api/

# Deployment on Render
Steps
1.	Push the project to GitHub:
2.	git init
3.	git add .
4.	git commit -m "First Commit"
5.	git branch -M master
6.	git remote add origin https://github.com/ginyele/hng12stage0.git
git push -u origin master
7.	Go to Render and create a New Web Service.
8.	Connect your GitHub repository.
9.	Use the following settings:
o	Runtime: Python
o	Build Command: pip install -r requirements.txt && python manage.py migrate
o	Start Command: gunicorn stage0task.wsgi --log-file -
10.	Click Deploy and wait for it to complete.
11.	Access your API at https://hng12stage0-3.onrender.com/api/
CORS Handling
The API includes CORS support via django-cors-headers. It allows requests from any origin:
