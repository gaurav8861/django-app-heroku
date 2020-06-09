# django-app-heroku
1. virtualenv django_env <br>
2. source django_env/bin/activate  <br>
3. pip install django <br>
4. django-admin.py startproject djangoherokuapp <br>
5. cd djangoherokuapp <br>
6. python manage.py startapp herokuapp <br>
7. Add 'herokuapp' to installed apps in settings.py <br>
8. python manage.py migrate <br>
9. python manage.py runserver <br>
10. heroku login <br>
11. touch Procfile > web: gunicorn djangoherokuapp.wsgi --log-file - <br>
12. Change djangoherokuapp to the name of your project to point to the location of the wsgi.py file <br>
13. runtime.txt > python-2.7.12 <br>
14. pip install gunicorn dj-database-url whitenoise psycopg2 <br>
15. pip freeze > requirements.txt <br>

```sh
dj-database-url==0.4.2
Django==1.11.7
gunicorn==19.7.1
psycopg2==2.7.3.2
pytz==2017.3
whitenoise==3.3.1
```

```sh
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] <br>

import dj_database_url  <br>
prod_db  =  dj_database_url.config(conn_max_age=500) <br>
DATABASES['default'].update(prod_db) <br>
```

16. heroku create herokudjangoapp <br>

```sh
ALLOWED_HOSTS = ['herokudjangoapp.herokuapp.com'] <br>
```

17. git init <br>
18. heroku git:remote -a herokudjangoapp <br>
19. git add . <br>
20. git commit -m "Initial commit" <br>
21. git push heroku master <br>

```sh
If you get an error message with collectstatic, simply disable it by instructing Heroku to ignore running the manage.py <br> collecstatic command during the deployment process. <br>

(django_env):~/Desktop/djangoherokuapp$ heroku config:set     DISABLE_COLLECTSTATIC=1   <br>
Setting DISABLE_COLLECTSTATIC and restarting ⬢ herokudjangoapp... done, v3   <br>
DISABLE_COLLECSTATIC: 1 <br>
```

22. git push heroku master <br>

23. heroku run python manage.py migrate <br>

```sh
#To load initial data 
python3 manage.py loaddata mysite/fixtures/dummy_data.json
```
