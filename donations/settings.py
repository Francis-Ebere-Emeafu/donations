"""
Django settings for donations project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c*#lf1)pwtjmayv-6hyl4y3+b*pyn-d=$7z^s$poh)3(=ci2@3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['staging.atheist.org.ng', 'www.atheist.org.ng', 'atheist.org.ng', 'localhost', '127.0.0.1', '167.172.156.45', 'atheist.everyday.com.ng']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'tinymce',
    'post_office',

    'news.apps.NewsConfig',
    'contact.apps.ContactConfig',
    'accounts.apps.AccountsConfig',
    'volunteer.apps.VolunteerConfig',
    'event.apps.EventConfig',
    'faq.apps.FaqConfig',
    'convention.apps.ConventionConfig',
    'payment.apps.PaymentConfig',
    'core.apps.CoreConfig',
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

ROOT_URLCONF = 'donations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.context_processors.news_items',
            ],
        },
    },
]

WSGI_APPLICATION = 'donations.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bayo_donation',
        'USER': 'bayo_clearcode',
        'PASSWORD': 'pass.p455',
        'PORT': ''
    }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "otherstatic"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, "media")

TINYMCE_INCLUDE_JQUERY = False
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'paste,table',
    'theme': 'advanced',
    'custom_undo_redo_levels': 10,
    'cleanup_on_startup': True
}


# Sending Email to registering members
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'asn_registrations'
EMAIL_HOST_PASSWORD = 'pass.p455'
DEFAULT_FROM_EMAIL = 'registrations@atheist.org.ng'
SERVER_EMAIL = 'registrations@atheist.org.ng'

EMAIL_BACKEND = 'post_office.EmailBackend'

# SMS
SMS_URL = 'https://api.infobip.com/sms/1/text/single'
SMS_USR = 'QRLabs'
SMS_PWD = 'pass.p455'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'payment': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'core': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

try:
    from local_settings import *
except ImportError:
    pass
