from .base_settings import *
import os
# import django_heroku

DEBUG = os.getenv('DEBUG', False) == 'True'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-b#1=qzk)w0!y2)cvh^#l8t&+gu=o!l7kg_#_uizgd&)w6ub&*i')


#middleware
MIDDLEWARE.insert(1,'whitenoise.middleware.WhiteNoiseMiddleware')

ALLOWED_HOSTS = ['*'] # allowing all hosts since security is not a major concern right now.
# #original
# STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# # Activate Django-Heroku.
# django_heroku.settings(locals())