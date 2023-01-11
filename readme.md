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

### File structure

```py
├─ base        # core of Django app (module)
│    ├─ migrations     # database migrations
│    ├─ static/base    # favicon, screenshots and CSS
│    ├─ templates/base # templates for rendering
│    ├─ admin.py       # adds models to admin panel
│    ├─ models.py      # definitions of models
│    ├─ urls.py        # app-wide URL path management
│    ├─ views.py       # logic used by URL paths
│    └─ ...            # various Django app files
├─ todo_list   # core of Django project
│    ├─ settings.py    # project's settings
│    ├─ urls.py        # URL path management
│    └─ ...            # various Django project files
├─ .gitattributes
├─ .gitignore
├─ db.sqlite3  # embedded SQLite database
├─ manage.py   # Django’s command-line utilities
└─ readme.md
```

# Examples (screenshots with hovertext)

### Adding new task

![before task creation](base/static/base/screenshots/task_deletion2.png "before task creation")
![task creation form](base/static/base/screenshots/add_new_task.png "task creation form")
![task creation result](base/static/base/screenshots/add_new_task2.png "task creation result")

### Task deletion

![before task deletion](base/static/base/screenshots/add_new_task2.png "before task deletion")
![task deletion screen](base/static/base/screenshots/task_deletion.png "task deletion screen")
![task deletion result](base/static/base/screenshots/task_deletion2.png "task deletion result")

### Themes

![dark theme with high contrast](base/static/base/screenshots/dark_contrast.png "dark theme with high contrast")
![dark theme](base/static/base/screenshots/dark.png "dark theme")
![light theme](base/static/base/screenshots/light.png "light theme")
![light theme with high contrast](base/static/base/screenshots/light_contrast.png "light theme with high contrast")

### Hiding by deadline

![before filtering by deadline](base/static/base/screenshots/dark_contrast.png "before filtering by deadline")
![setting deadline filter](base/static/base/screenshots/hide_by_deadline0.png "setting deadline filter")
![after setting filter but before activation](base/static/base/screenshots/hide_completed_1.png "after setting filter but before activation")
![deadline filtering result](base/static/base/screenshots/hide_by_deadline.png "deadline filtering result")

### Hiding completed

![before hiding](base/static/base/screenshots/hide_completed_1.png "before hiding")
![after hiding](base/static/base/screenshots/hide_completed_2.png "after hiding")

### Login client-side validation

![login client-side validation - no password](base/static/base/screenshots/login_validation.png "login client-side validation - no password")

### Registration client-side validation

![registration client-side validation - too short password](base/static/base/screenshots/register_validation1.png "registration client-side validation - too short password")
![registration client-side validation - digits-only password](base/static/base/screenshots/register_validation2.png "registration client-side validation - digits-only password")

### Filtering task by title

![before filtering](base/static/base/screenshots/text%20filtering.png "before filtering")
![after filtering](base/static/base/screenshots/text%20filtering2.png "after filtering")

### Updating an existing task

![before updating](base/static/base/screenshots/task_deletion2.png "before updating")
![updating form - initial](base/static/base/screenshots/update_task.png "updating form - initial")
![updating form - with changes](base/static/base/screenshots/update_task_2.png "updating form - with changes")
![result of updating](base/static/base/screenshots/update_task_3.png "result of updating")

### Normal and dense layout

![Normal layout](base/static/base/screenshots/normal_layout.png "Normal layout")
![Dense layout](base/static/base/screenshots/dense_layout.png "Dense layout")
