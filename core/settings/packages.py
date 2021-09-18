from django.conf import settings
from datetime import timedelta
import os

from .base import (
    INSTALLED_APPS,
    STATIC_ROOT,
    BASE_DIR
)
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# from decouple import config


# ############## #
#   EXTENSIONS   #
# ############## #

# Admin Documentation
INSTALLED_APPS.append('django.contrib.admindocs')
INSTALLED_APPS.append('django.contrib.sites')


# Django Rest Framework
INSTALLED_APPS.append('rest_framework',)
INSTALLED_APPS.append('coreapi',)
INSTALLED_APPS.append('drf_yasg',)


INSTALLED_APPS.append('safedelete',)
INSTALLED_APPS.append('django_filters',)

# Admin Interface
INSTALLED_APPS.append('admin_interface',)
INSTALLED_APPS.append('colorfield',)

# usefull commands
INSTALLED_APPS.append('django_extensions',)

# ############## #
# CUSTOM PROJECT #
# ############## #

# INSTALLED_APPS.append('todo')


# ############################# #
# CONFIG DJANGO ADMIN INTERFACE #
# ############################# #

X_FRAME_OPTIONS = 'SAMEORIGIN'


# #################### #
#      Extensions      #
# #################### #
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'utils.permissions.IsAuthenticatedAndActive',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'EXCEPTION_HANDLER': 'utils.exception_handler.custom_exception_handler',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=env('ACCESS_TOKEN_LIFETIME', cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=env('REFRESH_TOKEN_LIFETIME', cast=int)),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': env('SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'suid',
    'USER_ID_CLAIM': 'user_suid',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'core.urls.openapi_info',
    'DEFAULT_API_URL': 'https://api.todo.com/',
}


REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}
