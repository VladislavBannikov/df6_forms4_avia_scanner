from django.conf import settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b0e@^m&tccz11$w59qov$lhn-97!(%wfn-gray-c*x)^a$wx=2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = settings.INSTALLED_APPS + ['debug_toolbar',]
MIDDLEWARE = settings.MIDDLEWARE +['debug_toolbar.middleware.DebugToolbarMiddleware',]
INTERNAL_IPS = [
    '127.0.0.1',
]