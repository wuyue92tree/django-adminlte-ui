from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    select2_list_filter = ()
    search_field_placeholder = ''

    class Media:
        css = {
            "all": ("admin/components/select2/dist/css/select2.min.css",)
        }
        js = (
            "admin/components/select2/dist/js/select2.min.js",
        )

    def changelist_view(self, request, extra_context=None):
        view = super().changelist_view(request, extra_context)
        if hasattr(view, 'context_data'):
            cl = view.context_data.get('cl', None)
            if cl:
                cl.search_field_placeholder = self.search_field_placeholder
                filter_specs = cl.filter_specs

                for index, filter_spec in enumerate(filter_specs):
                    if filter_spec.field_path in self.select2_list_filter:
                        # flag to use select2
                        filter_spec.display_select2 = True
                        cl.filter_specs[index] = filter_spec
                view.context_data['cl'] = cl
        return view
