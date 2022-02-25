"""
ASGI config for WebHooks project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebHooks.settings')
django.setup()
application = get_asgi_application()


# uvicorn WebHooks.asgi:application --host '0.0.0.0' --port 8109 --reload
# systemctl daemon-reload && systemctl stop WebHooks.service && systemctl start WebHooks.service && systemctl status WebHooks.service
# systemctl stop WebHooks.service && systemctl start WebHooks.service
# systemctl start WebHooks.service
# systemctl status WebHooks.service