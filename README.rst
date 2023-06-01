django-adminlte-ui
==================

django admin theme base on adminlte

adminlte version: 2.4.18

install
=======

::

    pip install django-adminlte-ui

setup
=====

::

    INSTALLED_APPS = [
        'adminlteui',
        'django.contrib.admin',
        'django.contrib.auth',
        ...
    ]

Init models
===========

::

    python manage.py migrate django_admin_settings
