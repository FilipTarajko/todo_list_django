# Basic commands

### Starting the project as a development server:

1. Create a python environment with python and Django:
   - python 3.8.15 + Django 4.1.4 - version used for development
   - python 3.11.1 + Django 4.1.5 - the newest versions the project was tested on
1. Download and open project files within the environment
1. in cmd, run: `python manage.py migrate`
1. in cmd, run: `python manage.py runserver`
   > The server should now be running on 127.0.0.1:8000

### Creating a super user and opening administration panel:

1. in cmd, run: python manage.py createsuperuser
1. enter user data according to prompts
1. run server with python manage.py runserver
1. The administration panel located on 127.0.0.1:8000/admin should now allow access after logging in with previously entered data.
   > **Please note** that this user is created for administrative purposes and won't be properly initialized for using "standard", non-administrative features of the app. It can hovewer be changed by creating UsersSettings for the superuser account.

### Running project after initial setup:

```
python manage.py runserver
```

### Setting up migrations after changes in models:

```
python manage.py makemigrations
python manage.py migrate
```

# Design, features and details

### Nonexhaustive list of features:

- user registration and authorization based on Django's built-in solutions
- tasks stored in database
  - tasks can be created by any user, and are "owned" and only visible to their creator
  - all CRUD actions are available to the task's creator
  - users have no access to tasks they didn't create (403 Forbidden)
- settings stored in database, allowing for:
  - changing graphical themes (by adding different files with CSS variables to pages sent to browser)
  - filtering completed tasks
  - filtering tasks having deadline before any given date

### Data is stored using 3 models (classes defining data stored in DB):

- User - Django's built-in user model user for authentication
- Task - task model containing various data about tasks:
  - user - foreign key of user that created and "owns" the task
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

# Examples

### Adding new task

![task creation form](screenshots/add_new_task.png)
![task creation result](screenshots/add_new_task2.png)

### Task deletion

![task deletion screen](screenshots/task_deletion.png)
![task deletion result](screenshots/task_deletion2.png)

### Themes

![dark theme with high contrast](screenshots/dark_contrast.png)
![dark theme](screenshots/dark.png)
![light theme with high contrast](screenshots/light_contrast.png)
![light theme](screenshots/light.png)

### Hiding by deadline

![before filtering by deadline](screenshots/dark_contrast.png)
![setting deadline filter](screenshots/hide_by_deadline0.png)
![turning filtering by deadline on](screenshots/hide_by_deadline_1.png)
![deadline filtering result](screenshots/hide_by_deadline_2.png)

### Hiding completed

![without hiding completed](screenshots/hide_completed_1.png)
![with hiding completed](screenshots/hide_completed_2.png)

### Login client-side validation

![login client-side validation - no password](screenshots/login_validation.png)

### Registration client-side validation

![registration client-side validation - too short password](screenshots/register_validation1.png)
![registration client-side validation - digits-only password](screenshots/register_validation2.png)

### Filtering task by title

![Alt text](screenshots/text%20filtering.png)
![Alt text](screenshots/text%20filtering2.png)

### Updating an existing task

![before updating](screenshots/text_filtering.png)
![updating form - initial](screenshots/update_task.png)
![updating form - with changes](screenshots/update_task_2.png)
![result of updating](screenshots/update_task_3.png)
