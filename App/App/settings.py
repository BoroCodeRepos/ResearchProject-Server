"""
Django settings for App project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from threading import Event
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Date format for django-admin data representation
DATE_FORMAT = 'H:i:s d.m.Y'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c!s-0&czln#79l3!&u2f25n@13*v4c^vy(n&h2rjoqyn41!dfo'

# DEVICE TOKEN:
DEVICE_TOKEN = '1@r#(h=(m78ko5r8ebff*o4#aofihhp(ru1pj6tm731!m2oez_'

# DEVICE SERVER PORT AND CURRENT SERVER PORT
DEVICE_SERVER_PORT = 80
SERVER_PORT = 8000

# EVENT TO STOP CONNECTION TRACKING AFTER DISCONNECTING
CONNECTION_TRACKING_STOP_EVENT = Event()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_cleanup.apps.CleanupConfig',
    'django_extensions',
    
    'AboutUs.apps.AboutusConfig',
    'Dashboard.apps.DashboardConfig',
    'Device.apps.DeviceConfig',
    'Measurements.apps.MeasurementsConfig',
    'Logs.apps.LogsConfig',
    'Publications.apps.PublicationsConfig',
    'Sources.apps.SourcesConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'App.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "Templates/")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'App.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images) / Media files
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'Static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Static'),
    os.path.join(BASE_DIR, 'Media'),
]

MEDIA_URL = "Media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

# x-frame-options to displaying embed data

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default logout redirect url
# https://docs.djangoproject.com/en/4.2/ref/settings/#logout-redirect-url

LOGOUT_REDIRECT_URL = '/'

