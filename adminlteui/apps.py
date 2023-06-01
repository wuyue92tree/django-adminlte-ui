from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

__all__ = ['AdminlteUIConfig']


class AdminlteUIConfig(AppConfig):
    name = 'adminlteui'
    label = 'adminlteui'
    verbose_name = _('AdminLteUI')
