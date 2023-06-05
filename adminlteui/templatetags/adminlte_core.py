import importlib
from django import template
from adminlteui import version
from adminlteui.core import AdminlteConfig
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_adminlte_config_class():
    if hasattr(settings, 'ADMINLTE_CONFIG_CLASS'):
        m = '.'.join(settings.ADMINLTE_CONFIG_CLASS.split('.')[:-1])
        c = settings.ADMINLTE_CONFIG_CLASS.split('.')[-1]
        module = importlib.import_module(m)
        class_ = getattr(module, c)
        if not isinstance(class_(), AdminlteConfig):
            raise Exception(f'invalid AdminLteConfig class: {c}.')
        return class_()
    else:
        return AdminlteConfig()


@register.simple_tag
def get_adminlte_version():
    return version


@register.simple_tag
def eval_obj(request, string):
    """
    eval username_field or avatar_field from request object
    :param request:
    :param string:
    :return:
    """
    if string.startswith('request.') is False:
        raise Exception('string must startswith `request.` when call eval_obj.')
    return eval(string)
