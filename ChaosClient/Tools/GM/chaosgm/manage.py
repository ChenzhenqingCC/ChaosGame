#!/usr/bin/env python
import os
import sys
from django.conf import settings

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chaosgm.settings")

    settings.IS_RUN_SERVER = ('runserver' in sys.argv)
    from django.core.management import execute_from_command_line
    from scheduler import scheduler
    scheduler.start()
    execute_from_command_line(sys.argv)
