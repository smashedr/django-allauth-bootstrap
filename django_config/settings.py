import os
import logging
from configparser import ConfigParser
import allauth

allauth = allauth  # PEP8 compatibility

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, 'settings.ini')

config = ConfigParser()
config.read(CONFIG_FILE)

logging.basicConfig(
    filename=config.get('Logging', 'file'),
    level=logging.getLevelName(config.get('Logging', 'level')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'

allowed_hosts = config.get('App', 'allowed_hosts')
ALLOWED_HOSTS = allowed_hosts.split(' ')

DEBUG = config.getboolean('App', 'debug')
SECRET_KEY = config.get('App', 'secret')
STATIC_ROOT = config.get('App', 'static_root')

ROOT_URLCONF = 'home.urls'
WSGI_APPLICATION = 'django_config.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 2
LOGIN_REDIRECT_URL = "/oauth/"
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_AUTO_SIGNUP = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.discord',

    'home',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
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

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.' +
             'UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.' +
             'MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.' +
             'CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.' +
             'NumericPasswordValidator'},
]
