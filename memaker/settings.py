"""
Django settings for memaker project.

Generated by 'django-admin startproject' using Django 2.1.2.

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
# SECRET_KEY = ''
with open(os.path.join(BASE_DIR, 'static', 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

# For test, this comment needs to be discarded.
ALLOWED_HOSTS = ['127.0.0.1']
# For operational, this comment needs to be discarded.
# ALLOWED_HOSTS = ['memaker.co.kr','www.memaker.co.kr',
#                  'openfingers.com','www.openfingers.com',
#                  'ec2-13-209-5-163.ap-northeast-2.compute.amazonaws.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.sitemaps',

    'nested_admin',  # 추가 20190102

    'imagekit',
    'django.contrib.humanize',
    'easy_thumbnails',
    'widget_tweaks',

    'ckeditor',
    'ckeditor_uploader',
    'polls.apps.PollsConfig',  # 추가
    'intro.apps.IntroConfig',  # 추가
    'products.apps.ProductsConfig',  # 추가
    'lectures.apps.LecturesConfig',  # 추가
    'accounts.apps.AccountsConfig',  # 추가
    'boards.apps.BoardsConfig',  # 추가
]

SITE_ID = 1

###################################CK Editor Setting################################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = "files/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_REQUIRE_STAFF = False
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

# CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 300,
        'width': 'auto',
        'toolbar_Custom': [
            ['Styles', 'Format', 'FontSize', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Embed', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'Emoji', 'SpecialChar'], ['Source', 'CodeSnippet'],
        ],
        'extraPlugins': ','.join([
            'clipboard',
            'uploadimage',
            'image2',
            'pastefromword',
            'codesnippet',
            'embed',
        ]),
    }

}
AWS_QUERYSTRING_AUTH = False

######################################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'memaker.urls'

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

WSGI_APPLICATION = 'memaker.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-KR'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

ROOT_DIR = os.path.dirname(BASE_DIR)

STATIC_URL = '/static/'
# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    #'home/ubuntu/memaker/memaker/',
    # os.path.join(BASE_DIR, 'static'),
    STATIC_DIR
]

# set the log configuration with keeping Django default setting


MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%D/%B/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'memaker.log'),
            'formatter': 'verbose'
        },

    },
    'loggers': {
        'lectures': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'intro': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'products': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'polls': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
    },

}

# ses-smtp-user.20181231-105435
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.worksmobile.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'openfingers@openfingers.com'
with open(os.path.join(BASE_DIR, 'static', 'email_key.txt')) as e:
    EMAIL_HOST_PASSWORD = e.read().strip()
DEFAULT_FROM_EMAIL = 'help@openfingers.com'
