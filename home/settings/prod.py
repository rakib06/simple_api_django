'''Use this for production'''
from .local import *
import django_heroku
from .base import *
import dj_database_url
# from home.aws.conf import *

# WSGI_APPLICATION = 'home.wsgi.prod.application'
WSGI_APPLICATION = 'home.wsgi.prod.application'

CORS_ORIGIN_ALLOW_ALL = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DEBUG = True

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


'''
https://rk-mcq.herokuapp.com// | https://git.heroku.com/rkmcq.git
'''

STRIPE_SECRET_KEY = ''


# for heroku
if os.getcwd() == '/app':
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    # Honor the 'X-forwarded-Proto' header for request.is_secure().
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['https://df-api-islam.herokuapp.com']
    DEBUG = True
    

# Static asset configuration
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

django_heroku.settings(locals())

