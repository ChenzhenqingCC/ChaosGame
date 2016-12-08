"""
WSGI config for chaosgm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import chaosgm.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chaosgm.settings")
sys.path.append(chaosgm.settings.BASE_DIR) 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
