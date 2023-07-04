from django.contrib import admin


class DateRangeFilter(admin.FieldListFilter):
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
        else:
            self.lookup_val = None

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
