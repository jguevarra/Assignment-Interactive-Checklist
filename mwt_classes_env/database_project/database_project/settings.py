"""
Django settings for database_project project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=7blb@&rq705j_@&#+fd%-h8zxq#r1-71r6wo-ts_6v2&pyzy2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'database_project.urls'

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

WSGI_APPLICATION = 'database_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mwt_classes',
        'USER': 'mwt_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'test_mwt_classes',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#REFERENCES:

#Title:  How To Use PostgreSQL with your Django Application on Ubuntu 14.04
#Date: 12/10/2018
#Author: Justin Ellingwood
#Availability: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

#Title: How to migrate Django from SQLite to PostgreSQL
#Date: 12/10/2018
#Author: sirodoht
#Availability: https://gist.github.com/sirodoht/f598d14e9644e2d3909629a41e3522ad

#Title: How to start PostgreSQL on Windows
#Date: 12/10/2018
#Author: a_horse_with_no_name, Sean, Community, ALWAN, Santosh Patel, Matthew Lock, Nandan Chaturvedi, Tomasz Plonka
#Availability: https://stackoverflow.com/questions/36629963/how-to-start-postgresql-on-windows

#Title: How to connect from windows command prompt to mysql command line
#Date: 12/10/2018
#Author: washu, Ken White, Code Lღver, Raghvendra Parashar, Wilq, Paul Q. Alvarez, RonaldBarzell, Tomasz, ArifMustafa, et al.
#Availability: https://stackoverflow.com/questions/13752424/how-to-connect-from-windows-command-prompt-to-mysql-command-line
#Note:many authors on this thread, did not use all of them

#Title: First steps
#Date: 12/10/2018
#Availability: https://wiki.postgresql.org/wiki/First_steps

#Title: PostgreSQL 11 Documentation: ALTER USER
#Date: 12/10/2018
#Availability: https://www.postgresql.org/docs/current/sql-alteruser.html

#Title: Postgres user create database
#Date: 12/10/2018
#Author: bos, Philip Couling
#Availability: https://stackoverflow.com/questions/8988495/postgres-user-create-database/8989722#8989722

#Title: django test app error - Got an error creating the test database: permission denied to create database
#Date: 12/10/2018
#Author: Andrius, 3cheesewheel, Alasdair, George H., noufal valapra, Chandan, lmiguelvargasf
#Availability: https://stackoverflow.com/questions/14186055/django-test-app-error-got-an-error-creating-the-test-database-permission-deni

#Title: Permission denied for relation django_migrations using Heroku
#Date: 12/10/2018
#Author: drpm, Aur Saraf
#Availability: https://stackoverflow.com/questions/46679221/permission-denied-for-relation-django-migrations-using-heroku

#Title: Writing and running tests
#Date: 12/10/2018
#Availability: https://docs.djangoproject.com/en/2.0/topics/testing/overview/#the-test-database

#Title: 2.3.5.6 Starting MySQL from the Windows Command Line
#Date: 12/10/2018
#Author:  Jacob Nikom (User Commment on page, didn't really use)
#Availability: https://dev.mysql.com/doc/refman/8.0/en/windows-start-command-line.html
