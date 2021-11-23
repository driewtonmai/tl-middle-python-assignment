# tl-middle-python-assignment
TL Interview assignment

## Prerequisites

* Clone the project
`git clone https://github.com/driewtonmai/interview_task_polls.git`
* Create and start a a virtual environment
`virtualenv env --no-site-packages
source env/bin/activate`
* Install the project dependencies:
`pip install -r requirements.txt`
* Create a file named ".env"
`touch .env`
* Obtain a secret from MiniWebTool key and add to .env (you must use env_template template)
* Add .env to .gitignore file
* Then run
`python manage.py makemigrations`
`python manage.py migrate`
* Create admin account
`python manage.py createsuperuser`
* Load data from fixture
`python manage.py loaddata databasedump.json`
* Start the development server
`python manage.py runserver`

## Documentation

https://documenter.getpostman.com/view/9317614/UVJYKePb

## Built With

Django, django rest framework

### Authors

Omurzakov Tologon
