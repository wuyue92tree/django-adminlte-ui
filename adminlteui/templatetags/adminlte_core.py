import importlib
from django import template
from adminlteui import version
from adminlteui.core import AdminLteConfig
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_adminlte_config_class():
    if hasattr(settings, 'ADMINLTE_CONFIG_CLASS'):
        m = '.'.join(settings.ADMINLTE_CONFIG_CLASS.split('.')[:-1])
        c = settings.ADMINLTE_CONFIG_CLASS.split('.')[-1]
        module = importlib.import_module(m)
        class_ = getattr(module, c)
        if not isinstance(class_(), AdminLteConfig):
            raise Exception(f'invalid AdminLteConfig class: {c}.')
        return class_()
    else:
        return AdminLteConfig()


@register.simple_tag
def get_adminlte_version():
    return version
