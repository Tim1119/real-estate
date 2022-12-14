import environ
from pathlib import Path

env= environ.Env(DEBUG=(bool,False))


BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY=env('SECRET_KEY')
DEBUG=env("DEBUG")
ALLOWED_HOSTS=env('ALLOWED_HOSTS').split(" ")


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID=1 

THIRD_PARTY_APPS=[
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
]

LOCAL_APPS=[
    'apps.common',
    'apps.users',
    'apps.profiles',
    'apps.ratings'
]

INSTALLED_APPS = LOCAL_APPS+DJANGO_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real_estate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'real_estate.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/staticfiles/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIR = []
MEDIA_URL= "/mediafiles/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


import logging 
import logging.config 

from django.utils.log import DEFAULT_LOGGING 

logger = logging.getLogger(__name__)
LOG_LEVEL = "INFO"

logging.config.dictConfig({
    "version":1,
    "disable_existing_loggers":False,
    "formatters":{
        "console":{
            "format":"%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
        "file":{"format":"%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        "django.server":DEFAULT_LOGGING["formatters"]["django.server"],
    },
    "handlers":{
        "console":{
            "class":"logging.StreamHandler",
            "formatter":"console",
        },
        "file":{
            "level":"INFO",
            "class":"logging.FileHandler",
            "formatter":"file",
            "filename":"logs/real_estate.log",
        },
        "django.server":DEFAULT_LOGGING["handlers"]["django.server"],
    },
    "loggers":{
        "":{"level":"INFO","handlers":["console","file"],
        "propagate":False},
        "apps":{
            "level":"INFO","handlers":["console"],"propagate":False
        },
        "django.server":DEFAULT_LOGGING["loggers"]["django.server"]
    },
})