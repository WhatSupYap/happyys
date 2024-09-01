from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# 개발 환경에서만 Debug Toolbar를 활성화
if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]