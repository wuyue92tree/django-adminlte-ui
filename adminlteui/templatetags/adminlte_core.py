import importlib
from django import template
from adminlteui import version
from adminlteui.core import AdminLteConfig
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_adminlte_config_class():
    if hasattr(settings, 'ADMINLTE_CONFIG_CLASS'):
        return importlib.import_module(settings.ADMINLTE_SETTINGS)
    else:
        return AdminLteConfig()


@register.simple_tag
def get_adminlte_version():
    return version
