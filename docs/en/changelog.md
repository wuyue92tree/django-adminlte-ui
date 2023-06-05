# ChangeLog

## [v1.7.2](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.7.2)
- fix submit_row issue & make change form tools float
- improve fieldset.html & fix #15
- fix translate in `password_change_form.html`
- update `app.css`

## [v1.7.1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.7.1)
- fix exception when delete in changelist_view
- update docs

## [v1.7.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.7.0)
- make previous & next button effective on change_list.html
- use select2 make admin filter searchable
- add search_field_placeholder for search_fields
- use `github actions` replace `travis`

## [v1.6.1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.6.1)
- fix app in ADMINLTE_SETTINGS but current_user has not perm
- fix model in ADMINLTE_SETTINGS but current_user has not perm

## [v1.6.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.6.0)

- fix #26 case by modify list_per_page with '…' str
- add apps options in ADMINLTE_SETTINGS for menu icon & menu order
- update adminlte from 2.3.6 -> 2.4.18

## [v1.5.1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.5.1)

- fix template tag for Django 3;
- fix #18 image uploads cdn assets.

## [v1.5.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.5.0)

- fix #12 admin_static is removed in django3;
- add adminlte/widgets/select.html && auto active select2 by select id.

## [v1.4.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.4.0)

- feature #6 add `ADMINLTE_SETTINGS`;
- update menu render logic.

## [v1.3.3](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.3.3)

- add menu on the top;
- feature #3 add priority_level for menu order.

## [v1.3.2](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.3.2)

- add permission control for general_option & exchange_menu;
- update menuAction js fix menu issue;
- add gitter & demo;
- add show_avatar and avatar_field logic;
- add logged_out.html.

## [v1.3.1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.3.1)

- fix #2 get 500 when exchange menu;
- add .gitattributes.

## [v1.3.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.3.0)

- add exchange_menu logic with permission limit;
- add message when call exchange menu;
- update docs.

## [v1.3.0b1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.3.0b1)

- update models, content_type option add null=True;
- add js logic for menu;
- add exchange_menu logic without permission limit.

## [v1.3.0b0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.3.0b0)

- add treebeard as menu depends;
- add `select2` into `widgets.py`;
- update site_logo save path, base on settings.MEDIA_ROOT & settings.MEDIA_URL;
- fix base.html & login.html b tag issue;
- change base.html extra_style and extra_head position.

## [v1.2.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.2.0)

- add models with options;
- add general_option.html to manager general option;
- setup app label to `django_admin_settings`;
- register and add general_option into menu;
- add docs.

## [v1.1.1](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.1.1)

- fix filter and search issue at change_list.html, consult django-suit.

## [v1.1.0](https://github.com/wuyue92tree/django-adminlte-ui/releases/tag/1.1.0)

- add pages [ delete_selected_confirmation.html，add object_history.html，404.html，500.html]；
- update layout when fieldset.name is not none；
- update support default block extrahead extrastyle。
