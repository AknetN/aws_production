python3 -m venv env
source env/bin/activate
pip install django djangorestframework psycopg2-binary
django-admin startproject aws_project .


# ONE OF THE VARIANTS. THEN WE DELETED IT
# created folder settings
# DEBUG = False ---> add to development
# in manage,py choose proper environment: instead of     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_project.settings") use     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_project.settings.local") ----> local 9



# hide sensitive credentials:
# in line 24 in settings 
# add SECRET_KEY = os.environ.get("SECRET_KEY"), commented other secret_key
# create a new doc .env and add to it 'export SECRET_KEY'

python3 manage.py runserver
source .env

# added 
'''
STATIC_URL = "/static/"
STATIC_ROOT = "collections/static_collection" #
MEDIA_URL = "/media/"
MEDIA_ROOT = "collections/media"
'''
# created folder collections: media, static_collection
# make changed in DATABASES in settings.py

# add info to .env
# in urls.py add imports
# add if to urls.py

# read about whitenoise python here:https://whitenoise.readthedocs.io/en/stable/
#do everything from there

python3 manage.py runserver


pip install drf_spectacular
#add it to settings.py
# add to installed apps in settings:
'''
'rest_framework',
'drf_spectacular',
'''
# and add this at the end of settings.py:
'''REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.OpenApi.AutoSchema",
}'''

psql -h localhost -U postgres
CREATE DATABASE testdb;
\c testdb

source aws_project/.env

git add -A
git commit -m 'new production files'
git push origin aws_development 

# change DEBUG and ALLOWED_HOSTS in settings.py, add info to .env

# work at aws.amazon
# - ec2  ---> budget, instances
# - iam


sudo apt-get update
sudo apt-get upgrade
sudo apt-get install supervisor
sudo apt-get install -y nginx
sudo apt-get install python3-
sudo apt-get install python3-pip
sudo apt-get install python3-virtualenv
pip freeze > requirements.txt

git add -A
git commit -m 'after writing a hundred commands'
git pull origin main --no-rebase 
git status 
git log 
git push 
