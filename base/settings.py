"""
Django settings for untitled project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import secrets
#secrets.py contains passwords and secret keys, and is included in the .gitignore file, so you need to manually copy it

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),"..")

ADMINS = (
    ('Andrew Barr', 'wabarr@gmail.com'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEV = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["are-awesome.com"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'primatequiz',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
    #os.path.join(PROJECT_DIR,'personalWebsite/templates'),
    #os.path.join(PROJECT_DIR,'academicPhylogeny/templates'),
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mobi.middleware.MobileDetectionMiddleware',
)

ROOT_URLCONF = 'base.urls'

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if DEV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'primate_quiz.db'),
        }
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': "/home/wabarr/primate_quiz.db",
        }
    }
    

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

if DEV:
    STATIC_ROOT = "/Users/wab536/Desktop/static/"
else:
    STATIC_ROOT = "/home/wabarr/webapps/primates_are_awesome_static/"

STATICFILES_DIRS = (#'/home/wabarr/webapps/htdocs/',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,"base/static/base"),
    os.path.join(BASE_DIR,"primatequiz/static/primatequiz/images/"),

)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"


EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'wabarr'
EMAIL_HOST_PASSWORD = secrets.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = 'mail@wabarr.webfactional.com'
SERVER_EMAIL = 'mail@wabarr.webfactional.com'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}