# Guides

## General Option

custom your site by inheritance `adminlte.core.AdminLteConfig`.

```python
class AdminLteConfig(object):
    show_avatar = False
    avatar_field = 'request.user.avatar'

    site_logo = None
    site_header = 'AdminLteUI'

    skin = None

    search_form = True
    copyright = None
    welcome_sign = None
```


## ModelAdmin
- make change_list filter support select2
- custom placeholder for search_fields

```python
# adminlte/admin.py
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
    cl = view.context_data.get('cl')
    cl.search_field_placeholder = self.search_field_placeholder
    filter_specs = cl.filter_specs

    for index, filter_spec in enumerate(filter_specs):
      if filter_spec.field_path in self.select2_list_filter:
        # flag to use select2
        filter_spec.display_select2 = True
        cl.filter_specs[index] = filter_spec
    view.context_data['cl'] = cl
    return view
```

## Widgets

### AdminlteSelect

> Since v1.5.0b0, you don't need modify new template to active select2.

example:
```
# adminlte/admin.py
@admin.register(Menu)
class MenuAdmin(TreeAdmin):
    ...
    # change_form_template = 'adminlte/menu_change_form.html'
    formfield_overrides = {
        models.ForeignKey: {'widget': AdminlteSelect}
    }

# adminlte/menu_change_form.html
# active the target select
# {% extends 'admin/change_form.html' %}

# {% block extrajs %}
# {{ block.super }}
# <script>
#     django.jQuery('#id_content_type').select2();
# </script>
# {% endblock %}
```
effect:

![adminlte_select](https://github.com/wuyue92tree/django-adminlte-ui/blob/master/images/adminlte_select.png?raw=true)

### AdminlteSelectMultiple

> Since v1.5.0b0, you don't need modify new template to active select2.

example:
```
# adminlte/admin.py
@admin.register(Menu)
class MenuAdmin(TreeAdmin):
    ...
    # change_form_template = 'adminlte/menu_change_form.html'
    formfield_overrides = {
        # multiple for ManayToManyField
        models.ManayToManyField: {'widget': AdminlteSelectMultiple(
            attr={'style': 'width: 100%'}
        )}
    }

# adminlte/menu_change_form.html
# active the target select
# {% extends 'admin/change_form.html' %}

# {% block extrajs %}
# {{ block.super }}
# <script>
#     django.jQuery('#id_content_type').select2();
# </script>
# {% endblock %}
```
effect:

![adminlte_select](https://github.com/wuyue92tree/django-adminlte-ui/blob/master/images/adminlte_select_multiple.png?raw=true)


## Menu

