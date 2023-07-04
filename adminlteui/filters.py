import datetime

from django.contrib import admin, messages
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class DateRangeFilter(admin.FieldListFilter):
    # Reference https://github.com/andreynovikov/django-daterangefilter
    template = 'adminlte/date_range_filter.html'
    date_format = 'YYYY/MM/DD'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.field_name = field_path
        self.lookup_kwarg_gte = '{}__gte'.format(field_path)
        self.lookup_kwarg_lte = '{}__lte'.format(field_path)
        self.lookup_gte = params.get(self.lookup_kwarg_gte)
        self.lookup_lte = params.get(self.lookup_kwarg_lte)

        if self.lookup_gte == '':
            params.pop(self.lookup_kwarg_gte)

        if self.lookup_lte == '':
            params.pop(self.lookup_kwarg_lte)
        if self.lookup_gte and self.lookup_lte:
            self.lookup_val = '{} - {}'.format(self.lookup_gte, self.lookup_lte)
            # if we are filtering DateTimeField we should add one day to final date
            if "__" in field_path:
                related_model, field = field_path.split("__")
                field = model._meta.get_field(related_model).related_model._meta.get_field(field)
            else:
                field = model._meta.get_field(field_path)

            if isinstance(field, models.DateTimeField):
                try:
                    gte_date = datetime.datetime.strptime(self.lookup_gte, '%Y-%m-%d')
                    lte_date = datetime.datetime.strptime(self.lookup_lte, '%Y-%m-%d')
                    lte_date = lte_date + datetime.timedelta(seconds=3600 * 24 - 1)
                    if settings.USE_TZ:
                        gte_date = timezone.make_aware(gte_date, timezone.get_current_timezone())
                        lte_date = timezone.make_aware(lte_date, timezone.get_current_timezone())
                    params[self.lookup_kwarg_gte] = gte_date.strftime('%Y-%m-%d %H:%M:%S%z')
                    params[self.lookup_kwarg_lte] = lte_date.strftime('%Y-%m-%d %H:%M:%S%z')
                except ValueError:
                    messages.add_message(request, messages.ERROR,
                                         _("Invalid date for '%(field_name)s' field range filter") % {
                                             'field_name': field.verbose_name})
        else:
            self.lookup_val = ''

        super().__init__(field, request, params, model, model_admin, field_path)

    def choices(self, changelist):
        yield {
            'field_name': self.field_path,
            'value': self.lookup_val,
            'date_format': self.date_format,
            'query_string': changelist.get_query_string(remove=self._get_expected_fields())
        }

    def expected_parameters(self):
        return self._get_expected_fields()

    def _get_expected_fields(self):
        return [self.lookup_kwarg_gte, self.lookup_kwarg_lte]
