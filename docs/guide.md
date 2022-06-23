# Guides

## General Option

dynamic setup your site base on table `django_admin_settings_options`.

support options:

- Site Title
- Site Header
- Site Logo
- Welcome Sign
- Avatar Field
- Show Avatar

## Options

this options in your db, named `django_admin_settings_options`, after do migrate.

you can also add your custom option into this table, and use it by templatetags
 `adminlte_options` with function `get_adminlte_option`.

options table has a valid field to control your option work or not.


example:

```
# adminlte/general_option.html

{% load adminlte_options %}

# here my option_name is site_title, you can custom yourself.
{% get_adminlte_option 'site_title' as adminlte_site_title %}
{% if adminlte_site_title.valid %}
{{ adminlte_site_title.site_title }}
{% else %}
{{ site_title|default:_('Django site admin') }}
{% endif %}

```

before custom option, you should known what adminlte has used.

- site_title
- site_header
- site_logo
- welcome_sign
- USE_CUSTOM_MENU
- avatar_field
- show_avatar

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

Custom your menu depends on database && treebeard.

`depth 2` only, more will not effective now.

### Menu Setting

Exchange Menu by click the `Exchange Menu` button

![menu list](https://github.com/wuyue92tree/django-adminlte-ui/blob/master/images/menu-list.png?raw=true)

### Menu Form

![menu form](https://github.com/wuyue92tree/django-adminlte-ui/blob/master/images/menu-form.png?raw=true)

- name: The menu name
- position: The position of your custom menu, default `left`
- link_type:
    1. internal: django urls
    2. external: third part urls
    3. divide: link divide, like app verbose_name.
- link:
    1. `admin:index`: django url name, recommend.
    2. `/admin/`: django internal url, if you use i18n url, it's not a good choice.
    3. `http://`: outside url
- icon: [icon](https://adminlte.io/themes/AdminLTE/pages/UI/icons.html)
- content_type: Use for permission control, if user don't have permission to access the `app_label:model` in content_type, it will be skipped.
- valid: This menu item effective only when the valid is True.
- priority_level: default 100, use for ordering. `The bigger the priority`
- treebeard option: for order.

### get django url name for link

```

╰─$ python manage.py shell
Python 3.6.6 (default, Sep 29 2018, 19:18:41) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from django.urls import resolve                                                                                                                                             

In [2]: resolve('/zh-hans/admin/video/parsed/')                                                                                                                                     
Out[2]: ResolverMatch(func=django.contrib.admin.options.changelist_view, args=(), kwargs={}, 
url_name=video_parsed_changelist, app_names=['admin'], namespaces=['admin'], route=zh-hans/admin/video/parsed/)

```

django url name = namespaces:url_name

## settings
in your setting.py `ADMINLTE_SETTINGS`

### demo
Misleading demo features disabling/enabling
```python
ADMINLTE_SETTINGS = {
    'demo': True,
}
```

### search_form
Search form disabling/enabling

```python
ADMINLTE_SETTINGS = {
    'search_form': True,
}
```

### skin
Skin choice
```python
ADMINLTE_SETTINGS = {
    'skin': True,
}
```

### copyright
Customer-specific copyright notice
```python
ADMINLTE_SETTINGS = {
    'copyright': 'John Smith',
}
```

### navigation_expanded
Navigation expanded feature, making navigation elements not being hidden under openable menu
```python
ADMINLTE_SETTINGS = {
    'navigation_expanded': True,
}
```

### show_apps
```python
ADMINLTE_SETTINGS = {
    'show_apps': ['django_admin_settings', 'auth', 'main'],
}
```
### main_navigation_app
Main navigation app feature, where app models are put on top of the menu
```python
ADMINLTE_SETTINGS = {
    'main_navigation_app': 'django_admin_settings',
}
```

### apps
Modify apps icon & order apps/models

```python
ADMINLTE_SETTINGS = {
    'example-app': {
        'icon': 'fa-desktop',
        'models': {
            'example-model': {
                'icon': 'fa-archive'
            },
            'example-model1': {}
        }
    },
    'auth': {
        'icon': 'fa-users'
    }
}
```