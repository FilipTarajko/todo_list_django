Starting the project as a development server:

1. Create a python environment with python and Django:
   python 3.8.15 + Django 4.1.4 - version used for development
   python 3.11.1 + Django 4.1.5 - the newest versions the project was tested on
1. Download and open project files within the environment
1. in cmd, run: python manage.py migrate
1. in cmd, run: python manage.py runserver
   The server should now be running on 127.0.0.1:8000

Creating a super user and opening administration panel:

1. in cmd, run: python manage.py createsuperuser
1. enter user data according to prompts
1. run server with python manage.py runserver
   The administration panel located on 127.0.0.1:8000/admin should now allow access after logging in with previously entered data. Please note that this user is created for administrative purposes and won't be properly initialized for using "standard", non-administrative features of the app. It can hovewer be changed by creating UsersSettings for the superuser account.

Running project after initial setup:
python manage.py runserver

Setting up migrations after changes in models:
python manage.py makemigrations
python manage.py migrate

Data is stored using 3 models (classes defining data stored in DB):

- User - Django's built-in user model user for authentication
- Task - task model containing various data about tasks:
  - user - foreign key of user that owns the task
  - title - title of the task
  - description - (optional) text field user for storing any additional text data about the task
  - complete - boolean field, can be used for task filtering
  - deadline - (optional) deadline date that can be later used for task filtering
  - created - automatically filled date of task creation
- UsersSettings
  - user - foreign key of user whose settings are being stored in the object
  - darkmode - boolean field for switching between light and dark themes
  - hide_complete - boolean field for hiding tasks with True in "complete" field
  - high_contrast - boolean field for switching between normal- and high-contrast themes
  - filter_by_deadline - boolean field for turning task filtration by deadline on/off
  - users_display_after_day - datetime field based on which the task-by-deadline filtration takes place when filter_by_deadline is set to True
