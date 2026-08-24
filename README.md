# SkillMatch - Graph-Based Job Recommendation System

SkillMatch is a Django-based job recommendation application that uses a graph database to match a user's technical skills with relevant job opportunities.

The system analyzes the relationship between skills, jobs, and companies to recommend suitable career opportunities and identify missing skills.

## Features

- Select multiple technical skills
- Graph-based job recommendations
- Match percentage for each job
- Display matching skills
- Display missing skills
- Company-wise job recommendations
- Professional responsive user interface
- CognoDB/Neo4j graph database integration
- Django backend
- Secure environment-variable based database configuration

## Technology Stack

- Python
- Django
- CognoDB / Neo4j
- Cypher
- HTML
- CSS
- python-dotenv
- Git & GitHub

## Application Flow

User selects skills

        ↓

Django application

        ↓

CognoDB graph database

        ↓

Skills → Jobs → Companies

        ↓

Calculate skill match

        ↓

Recommended jobs

## Graph Model

The application represents career information as a graph:

Candidate
    |
    | HAS_SKILL
    ↓
Skill
    ↑
    | REQUIRES
    |
Job
    |
    | OFFERED_BY
    ↓
Company

This graph structure makes it easier to traverse relationships between skills, jobs, candidates, and companies.

## Project Structure

skillmatch-django-cognodb/

├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── recommendations/
│   ├── views.py
│   ├── database.py
│   └── ...
│
├── scripts/
│   └── seed.py
│
├── skillmatch/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── templates/
    └── recommendations/
        └── index.html

## Setup

### 1. Clone the repository

git clone https://github.com/kirthy20/Skill_Match_cognodb.git

cd Skill_Match_cognodb

### 2. Create a virtual environment

python -m venv wexa

### 3. Activate the environment

Windows:

wexa\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure environment variables

Create a `.env` file in the project root.

Use `.env.example` as a template:

COGNODB_URI=your_cognodb_uri
COGNODB_USERNAME=your_username
COGNODB_PASSWORD=your_password

Do not commit the `.env` file to GitHub.

### 6. Seed the database

python -m scripts.seed

### 7. Run the Django server

python manage.py runserver

Open:

http://127.0.0.1:8000/

## Example

A user can select skills such as:

- Python
- SQL
- Excel
- Power BI
- Java
- Git

The system then calculates which jobs have the highest skill overlap.

Example:

Data Analyst

Match: 75%

Matching Skills:
- Python
- SQL
- Power BI

Missing Skills:
- Excel

## Future Improvements

- User authentication
- Personalized candidate profiles
- Job location filtering
- Experience-level filtering
- Skill learning recommendations
- Job application tracking
- Hosted production deployment

## Author

Keerthi
