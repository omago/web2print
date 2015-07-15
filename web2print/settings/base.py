"""
Django settings for web2print project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g3vesr(6@y6=yqi-kj_l0ywptj&0z+qn7bgim#k2-gphl!%nub'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    "core/templates",
    "layout",
    "templates",
)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    "south",
    "core",
    'layout',
    "product_category",
    "product_subcategory",
    "banner",
    "banner_position",
    "product",
    "article_category",
    "article",
    "user",
    "cart",
    "format",
    "paper",
    "paper_type",
    "paper_finish",
    "paper_weight",
    "insert_price",
    "printer",
    "printing_price",
    "press",
    "plastic",
    "cart_product",
    "cart",
    "finish",
    "finish_price",
    "finish_type",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'product_category.product_category_context_processor.product_categories',
    'article.article_context_processor.informations',
#     'banner.banner_context_processor.bottom_large_banner',
#     'banner.banner_context_processor.bottom_left_small_banner',
#     'banner.banner_context_processor.bottom_left_small_banner',
)

ROOT_URLCONF = 'web2print.urls'

WSGI_APPLICATION = 'web2print.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'hr-HR'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

APPLICATION_NAME = "Administracija"
APPLICATION_VERSION = "1.0"

HAS_FRONTEND = True

RESULTS_PER_PAGE = 30
LOGIN_URL = '/admin/account/login'

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60*60*8*30

AUTH_USER_MODEL = 'user.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (

)

MEDIA_ROOT = PROJECT_ROOT + "/uploads/"
MEDIA_URL = "/uploads/"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)