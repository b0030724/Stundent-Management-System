"""
Django settings for my_django_project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
WEBSITE_HOSTNAME = os.environ.get['WEBSITE_HOSTNAME']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = WEBSITE_HOSTNAME == None

ALLOWED_HOSTS = [] if DEBUG else [WEBSITE_HOSTNAME]

if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [f'https://{WEBSITE_HOSTNAME}']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',    
    'students',
    'crispy_forms',
    'crispy_bootstrap4',
    'storages'
    
    
]
LOGIN_URL = 'students:login'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4' 
LOGOUT_REDIRECT_URL = '/login/'  


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'ed37add6c0e1e2'
EMAIL_HOST_PASSWORD = '94476ae954d80f'
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'students' / 'templates' / 'students'],
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

WSGI_APPLICATION = 'my_django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['AURE_DB_NAME'],
        'PORT': os.environ['AURE_DB_PORT'],
        'HOST': os.environ['AURE_DB_HOST'],
        'USER': os.environ['AURE_DB_USER'],
        'PASSWORD': os.environ['AURE_DB_PASSWORD'],
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
#STATIC_URL = '/static/'

# The directory where static files will be collected for production
#STATIC_ROOT = BASE_DIR / 'staticfiles'

# Additional locations of static files
#STATICFILES_DIRS = [
   # BASE_DIR / 'static',  # For my static files in the root `static` directory
    #BASE_DIR / 'students/static'  # For static files within the `students` app   
#]
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "connection_string": os.environ['AURE_DB_CONN'],
            "azure_container": "media",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "connection_string": os.environ['AURE_DB_CONN'],
            "azure_container": "static",
        },
    },
}


STATIC_URL = 'https://b0030724dcbs.blob.core.windows.net/static/'
MEDIA_URL = 'https://b0030724dcbs.blob.core.windows.net/media/'
# Media files (Uploaded images)
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
