# django-app-heroku
virtualenv django_env <br>
source django_env/bin/activate
pip install django
django-admin.py startproject djangoherokuapp
cd djangoherokuapp
python manage.py startapp herokuapp
Add 'herokuapp' to installed apps in settings.py
python manage.py migrate
python manage.py runserver

heroku login
touch Procfile > web: gunicorn djangoherokuapp.wsgi --log-file -
Change djangoherokuapp to the name of your project to point to the location of the wsgi.py file
runtime.txt > python-2.7.12
pip install gunicorn dj-database-url whitenoise psycopg2
pip freeze > requirements.txt

dj-database-url==0.4.2
Django==1.11.7
gunicorn==19.7.1
psycopg2==2.7.3.2
pytz==2017.3
whitenoise==3.3.1

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
]

import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

heroku create herokudjangoapp
ALLOWED_HOSTS = ['herokudjangoapp.herokuapp.com']
git init
heroku git:remote -a herokudjangoapp
git add .
git commit -m "Initial commit"
git push heroku master

If you get an error message with collectstatic, simply disable it by instructing Heroku to ignore running the manage.py collecstatic command during the deployment process.

(django_env):~/Desktop/djangoherokuapp$ heroku config:set     DISABLE_COLLECTSTATIC=1  
Setting DISABLE_COLLECTSTATIC and restarting ⬢ herokudjangoapp... done, v3  
DISABLE_COLLECSTATIC: 1

git push heroku master

heroku run python manage.py migrate
