# -*- coding: utf-8 -*-
# Base django settings for aptest project

from os.path import join, dirname

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Simeon Movchan', 'simeon.movchan@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'aptest.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SITE_ID = 1

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Yekaterinburg'


USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ROOT = dirname(dirname(__file__))

STATIC_ROOT = join(SITE_ROOT, 'static')
MEDIA_ROOT = join(SITE_ROOT, 'upload')

STATIC_URL = '/~static/'
MEDIA_URL = '/~upload/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'aptest.urls'

WSGI_APPLICATION = 'aptest.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'mptt',
    'south',

    'aptest',
    'debug_toolbar',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

FORCE_SCRIPT_NAME = ''

INTERNAL_IPS = [
    '127.0.0.1',
]

PAGE_NAME_RE = ur'[a-zA-Zа-яА-Я0-9_]+'
PAGE_PATH_RE = ur'(?:%s/)+' % PAGE_NAME_RE

try:
    from localsettings import *
except ImportError:
    pass
