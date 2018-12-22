"""
WSGI config for bad_fortune_cookie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bad_fortune_cookie.settings')

application = get_wsgi_application()
