"""
Django settings for LearningAssess project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import configparser
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@8xed9&uqk&)@8)6(*!!w7kz3p(8y*1-9r##_%_%ky6(=s^5&8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '0.0.0.0']
BASE_CONFIG = configparser.ConfigParser()
BASE_CONFIG.read('config.ini')
MYSQL_SETTINGS = BASE_CONFIG['MYSQL_SETTINGS']
REDIS_SETTINGS = BASE_CONFIG['REDIS_SETTINGS']
MINI_PROGRAM = BASE_CONFIG['MINI_PROGRAM']
OSS_SETTINGS = BASE_CONFIG['OSS_SETTINGS']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'apps.tiku',
    'apps.wechat',
    'apps.config',
    'apps.index',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader'  # 富文本编辑器上传图片模块
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

ROOT_URLCONF = 'LearningAssess.urls'
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'LearningAssess.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": MYSQL_SETTINGS['db'],
        "USER": MYSQL_SETTINGS['user'],
        "PASSWORD": MYSQL_SETTINGS['passwd'],
        "HOST": MYSQL_SETTINGS['host'],
        "PORT": int(MYSQL_SETTINGS['port']),
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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static/"),
# ]
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Redis Cache Config
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION":
            f"redis://{REDIS_SETTINGS['host']}:{REDIS_SETTINGS['port']}/"
            f"{REDIS_SETTINGS['db']}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_SETTINGS['passwd'],
            "CONNECTION_POOL_KWARGS": {"max_connections": 128}
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# REST FRAMEWORK
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'propagate': True,
        #     'level': 'DEBUG',
        # },
    }
}
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8181",
    "http://localhost:8181",
    "http://119.23.111.230:8000",
    "https://dati.runjiahui.cn",
    "http://dati.runjiahui.cn",
    "http://172.30.53.122:8000",
    "https://xlzx.shuchenlin.com",
    "http://xlzx.shuchenlin.com",
]
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Image'],
        ],
        # 'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        'width': 800,  # 编辑器宽
    },
}

CKEDITOR_UPLOAD_PATH = 'uploads'  # 上传图片保存路径，如果没有图片存储或者使用自定义存储位置，那么则直接写  ' ' ,
CKEDITOR_ALLOW_NONIMAGE_FILES = False
# 如果是使用django本身的存储方式，那么你就指名一个目录用来存储即可。

OSS_ACCESS_KEY_ID = OSS_SETTINGS['access_key']
OSS_ACCESS_KEY_SECRET = OSS_SETTINGS['access_secret']
OSS_ENDPOINT = OSS_SETTINGS['endpoint']
OSS_BUCKET_NAME = OSS_SETTINGS['bucket_name']
OSS_CDN_NETLOC = OSS_SETTINGS['cdn_netloc']
