### Start a django project
* first time to create project, no need to run this once the project is created: django-admin startproject piglatin
* go to the project folder
* run localhost server: pyhton3 manage.py runserver

### Note
* python3.7 is not supported by django 1.11.x
* wsgi.py and settings.py are just some top level settings about the app
* urls.py is used to decide which specific url would be routed to which content/page, like traffic management, this is the file that we would mainly work on
* templates is where to put html files and need to update TEMPLATES list with DIR key in settings.py correspondingly
