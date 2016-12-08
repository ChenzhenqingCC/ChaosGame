"""
Django settings for chaosgm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static'),
]

MAX_NOTICE_LEN = 30000
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used  in production secret!
SECRET_KEY = 'pmuanrtpxkuzp8!lqbt=)&g1rwn&co%hshbn*1n37g#_k#2qh^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

IS_RUN_SERVER = False

ALLOWED_HOSTS = []

DEFAULT_CHARSET = "utf-8"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'timezone_field',
    'gm',
	'notice',
	'ban',
    'flashnews',
    'account',
    'gamemail',
    'server',
    'js_locale',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'gm.models.TimezoneMiddleware'
)

ROOT_URLCONF = 'chaosgm.urls'

WSGI_APPLICATION = 'chaosgm.wsgi.application'

GM_PORT_ADD = 100


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'datebase.sqllite'),
        'USER':'maplegame',
        'PASSWORD':'10maplegame13',
    }
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'chaosgm.wsgi.application'

