# django-app-heroku
virtualenv django_env <br>
source django_env/bin/activate  <br>
pip install django <br>
django-admin.py startproject djangoherokuapp <br>
cd djangoherokuapp <br>
python manage.py startapp herokuapp <br>
Add 'herokuapp' to installed apps in settings.py <br>
python manage.py migrate <br>
python manage.py runserver <br>

heroku login <br>
touch Procfile > web: gunicorn djangoherokuapp.wsgi --log-file - <br>
Change djangoherokuapp to the name of your project to point to the location of the wsgi.py file <br>
runtime.txt > python-2.7.12 <br>
pip install gunicorn dj-database-url whitenoise psycopg2 <br>
pip freeze > requirements.txt <br>

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
] <br>

import dj_database_url  <br>
prod_db  =  dj_database_url.config(conn_max_age=500) <br>
DATABASES['default'].update(prod_db) <br>

heroku create herokudjangoapp <br>
ALLOWED_HOSTS = ['herokudjangoapp.herokuapp.com'] <br>
git init <br>
heroku git:remote -a herokudjangoapp <br>
git add . <br>
git commit -m "Initial commit" <br>
git push heroku master <br>

If you get an error message with collectstatic, simply disable it by instructing Heroku to ignore running the manage.py <br> collecstatic command during the deployment process. <br>

(django_env):~/Desktop/djangoherokuapp$ heroku config:set     DISABLE_COLLECTSTATIC=1   <br>
Setting DISABLE_COLLECTSTATIC and restarting ⬢ herokudjangoapp... done, v3   <br>
DISABLE_COLLECSTATIC: 1 <br>

git push heroku master <br>

heroku run python manage.py migrate <br>
