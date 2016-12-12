"""
Django settings for GLMS project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/"""

# from .email_info import *
# EMAIL_USE_TLS = EMAIL_USE_TLS
# EMAIL_HOST = EMAIL_HOST
# EMAIL_HOST_USER = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
# EMAIL_PORT = EMAIL_PORT


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hoype27v!_-1-aie!!caa6l9k#et2132xhb)rz4=8ky1&)(9xl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['.gktcs.in',]

EMAIL_HOST = 'mail.gktcs.in'
EMAIL_HOST_PASSWORD = 'Sgipl09@2015'
EMAIL_HOST_USER = 'support@gktcs.in'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
SERVER_EMAIL = 'support@gktcs.in'
DEFAULT_FROM_EMAIL = 'GKTCS Support <support@gktcs.in>'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#	'django_user_agents',
#	'tracking_analyzer',
    'lms',
	#crispy
	'crispy_forms',
    #redux apps
    #'django.contrib.sites',
    'registration',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'GLMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['Template'],
		'DIRS': [os.path.join(BASE_DIR, 'Template')],
        'APP_DIRS': True,
        'OPTIONS': {
          'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.csrf',
            ],
        },
    },
]

#STATIC_URL = '/static/'
#TEMPLATE_DIRS=(os.path.join(BASE_DIR,'Template'),)
#STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

WSGI_APPLICATION = 'GLMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gipldb',
        'USER':'gipl',
        'PASSWORD':'Gipl@2015',
        'HOST':'localhost',
        'PORT':'3306',
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
MEDIA_ROOT = '/home/gktcs/public_html/GLMS/public/static/placement/'
MEDIA_URL = 'http://gktcs.in/GLMS/public/static/placement/'
STATIC_URL = 'http://gktcs.in/GLMS/public/static/'
STATIC_ROOT = '/home/gktcs/public_html/GLMS/public/static/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# redux
ACCOUNT_ACTIVATION_DAYS = 7

REGISTRATION_AUTO_LOGIN = True

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

REGISTRATION_FORM = 'lms.forms1.Custom_registeration_form'

#GOIP_PATH = os.path.join(BASE_DIR, "geoip")