from __future__ import unicode_literals

from django.apps import AppConfig
from django.conf import settings
from importlib import import_module
from django.utils.module_loading import module_has_submodule
import manage
from django.conf import settings


class GmConfig(AppConfig):
    name = 'gm'

    def ready(self):
        def autoload(submodules):
            for app in settings.INSTALLED_APPS:
                mod = import_module(app)
                for submodule in submodules:
                    try:
                        name = "{}.{}".format(app, submodule)
                        import_module(name)
                        print('run ' + name)
                    except Exception, e:
                        if module_has_submodule(mod, submodule):
                            raise

        if settings.IS_RUN_SERVER:
            autoload(["startup"])
