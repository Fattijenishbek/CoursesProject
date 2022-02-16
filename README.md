# CoursesProject

## A small tutorial from the beginning till DEF that I wrote for myself

**pip install django** to install django, if it’s already installed than it will say that requirements are satisfied.

**Virtual environment**  is like a different box in our PC, it allows us to work with different versions of python without conflict. Inside environment we can install django, or work with specific version of python that we need.

**pip install virtualenvwrapper**  installs virtual environment wrapper

**mkvirtualenv name_of_env** to create virtual environment, ex: mkvirtualenv myapp. We can create virtual environment even with the specific version of python. 

**deactivate**  to deactivate the virtual environment and go to usual terminal

rmvirtualenv name_of_env  to delete or remove the virtual environment

**django-admin startproject project_name** to create the project	

**source virtualenvwrapper.sh** to start working with virtual environment commands if it’s not set in bash_profile(home)

Many people use the virtualenvwrapper tool, which keeps all virtualenvs in the same place (the ~/.virtualenvs directory) and allows shortcuts for creating and keeping them there. For example, you might do:
**mkvirtualenv djangoproject**
and then later:
**workon djangoproject**


**which python** to see which python are we using now

pip list  to see wht kind of packages are installed in specific version of python, or what kind of packages are allowed us to use(for ex: maybe in our laptop downloaded python or python in virtual environment)

**Django-project can contain many Django-apps, or django-app is like a subset of Django-project:**  we have one main project and multiple apps for each purpose in the project. One project and one app at least. apps we will create in the root directory - the directory where managa.py is contained. The file manage.py we use a lot for different things, even we don’t make changes in it a lot at the beginning. For example creating an app is one of the reason to use manage.py file. 

**python manage.py startapp name_of_app** to create app in project(should be in root directory)

**models.py** is the file where we create all our database

admin.py is the file that allows us to control or maintain our site or database, everything we need to know about our database.

**Views.py** is the file where all main things are happen 

**python manage.py runserver** to run the project, here we also use manage.py file

what we have done in apps - which is a subset of the project, we should tell the project, too, what are we looking for in app(path). Otherwise it won’t notice it. We do that in the project’s URLs, with include.

templates folder  should be created in root directory so that we could store our HTML files. And we will tell the project django that we are gonna use that folder in our project, by adding templates  in project’s settings.py file, where templates -> DIRS(stands for directories)-> [BASE_DIR, ‘the name of the folder’] where HTML files stored. Then it will look files that stored in that folder

**sudo fuser -k 8000/tcp to stop running servers in background/all. For osx users you can use sudo lsof -t -i tcp:8000 | xargs kill -9**

static file in django is any external file that we use in our template file

BASE_DIR the folder which contains manage.py file

STATICFILES_DIRS to configure (or tell the django where to look for the static files) in project’s settings.py file

in models.py file in app, in order to convert basic class to model we should add in braces (models.Model) and we won’t need id attribute anymore coz the model will create it automatically. To specify types: instead str write models.CharField(max_lenght=n), use = instead : -> name = models.CharField(), not name: models.CharField()

by default Django uses sqlite database, but we will cover also how to work with pgAdmin

to send fields into our database: 
1) we should register our app in main project: main_project’s settings.py file -> INSTALLED_APPS, add there your app, from where we gonna migrate our fields.
2) then migrate that data into our database: through terminal, project folder, root directory where manage.py file is available, python manage.py makemigrations to save any changes in models.py file. to send that changes to our database: python manage.py migrate(we should repeat these commands if we made changes in our model)

to manipulate our data through admin panel we should create superuser or adminuser:                         python manage.py createsuperuser

in app’s admin.py file we will register our models, after what we won’t have to manipulate(add or delete) data manually through code, and just by admin panel. so, to register model in admin panel: from .models import “Your Model” -> admin.site.register(Your Mode)


connect project with postgreSQL:
Download postgresql and pgAdmin.
Create database in pgadmin
In settings.py file: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER':'postgres',
        'PASSWORD': ‘psql', //will write later
        'HOST':'localhost'
    }
}

through cmd install two libraries(without which we can’t connect postgresql with out project): pip install psycopg2(to connect everything), pip install Pillow(to connect related to images and other files). After installing these two we should write PASSWORD IN DATABASE in settings.py file.


to protect our sensitive data in our django project we use Python Decouple Library. Create .env file in project folder where manage.py file is available. There we will create variables which we will use in settings.py file. In settings.py file from decouple import config. Then change everything with variables in .env file. Ex: SECRET_KEY = config(‘SECRET_KEY’) 


find . -name “*.pyc” -print to see all files with .pyc extensions. Instead -print we also can use -delete 

git Wildcard info:
- # - marks line as a comment
- * - matches 0 or more characters
- ? - matches 1 character
- [abc] - matches a, b, _or_ c
- ** - matches nested directories - a/**/z matches
--- a/z
--- a/b/z
--- a/b/c/z

git command used in this video:
- git add .
- git commit -m "Commit Description"
- git push origin [Name of Branch]
- git rm -rf --cached .


Django RST Framework  is a library which allows us to build APIs in our Django project

drf stands for Django Rest Framework 

**pip install djangorestframework**  to install restframework. 

we can create views.py file in project itself, and not only in app it should be. There: 
from django.shortcuts import render with render we could just render the template file, but in order to render API we import from rest_framework.views import APIView the ready api view which helps us to create API in our project. Also from rest_framework.response import Response so that we could return the data as response. 

in urls.py we should import views so that we could access them while creating paths. If we have class in views.py file or we call class based view, when we use it in urls.py, we should write .as_view() as well(TestView.as_view()), then use its functions. Or if we have function based view, there is no need to use .as_view(). 

So that rest-framework recognizes, we should write one more path with include: path(‘api-auth/’, include(‘rest_framework.urls’), it must be without any spaces

**serializers in Django Rest Framework** is a structure of representation that represents a data, we want to return in a JSON formant or saved in JSON format. So we can easily transform Django modules into JSON.

to implement serialization:
create app in project
create serializers.py file in app ( there: from rest_framework import serializers, from .models import Student(model that we created). Create class Class_NameSerializer(serializers.ModelSerializer):
class Meta:
model = Student(our model)
Fields = (‘name’, ‘age’) fields that we want to use
then create a model in models.py file
register our app in project’s settings.py file
install postman with this command: sudo snap install postman
to create api with authentication in project’s views.py file we should import: from res_framework.permissions import IsAuthenticated. Before any functions below after class we should add permission_classes = (IsAuthenticated,) , and leave blank or just remove all if everybody can access.

to set this authentications we need to add REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication'
    ]
} at the bottom of the settings.py file. Also, add ‘rest_framework.authtoken’ in Installed_apps in settings.py file.

python manage.py flush flush or clear all the data we have in the database

python manage.py drf_create_token admin(it’s a username for which we are creating token)
In postman url-> get or post any method -> authorization -> select API key -> Key=Authorization (default for django) value= Token and created token for user -> add to = Header 
