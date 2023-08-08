"""
ASGI config for xops project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

profile = os.environ.get("NOAH_DEVOPS_PROFILE", "develop")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'xops.settings.{profile}')

application = get_asgi_application()
