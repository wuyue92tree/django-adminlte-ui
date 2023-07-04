import logging
import django
from django import template
from django.contrib.admin import AdminSite
from django.http import HttpRequest
from adminlteui.templatetags.adminlte_core import get_adminlte_config_class

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

try:
    from django.urls import reverse, resolve
except ImportError:
    from django.core.urlresolvers import reverse, resolve

register = template.Library()

if django.VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


def render_main_menu(menu):
    if not menu:
        return ''
    html = ''
    for menu_item in menu:
        child = menu_item.get('child', [])
        if child:
            if menu_item.get('active') is True:
                treeview_class = 'treeview active menu-open'
                treeview_menu_class = 'treeview-menu menu-open'
            else:
                treeview_class = 'treeview'
                treeview_menu_class = 'treeview-menu'
            menu_item_html = f'''
            <li class="{treeview_class}">
                <a href="javascript:void(0)">
                    <i class="fa {menu_item.get('icon')}"></i>
                    <span style="overflow: hidden; display: inline-block; vertical-align:top;">{menu_item.get('name')}</span>
                    <span class="pull-right-container"><i class="fa fa-angle-left pull-right"></i></span>
                </a>
                <ul class="{treeview_menu_class}">
                    {render_main_menu(child)}
                </ul>
            </li>
            '''
        else:
            target_blank = '' if menu_item.get('target_blank') is False else 'target="_blank"'
            flag = 'active' if menu_item.get('active') is True else ''
            menu_item_html = f'''
            <li class="{flag}"><a {target_blank} href="{menu_item.get('url')}"><i class="fa {menu_item.get('icon')}"></i><span> {menu_item.get('name')}</span></a></li>
            '''
        html += menu_item_html
    return html


def render_top_menu(menu):
    """
    render top menu
    top menu will ignore icon
    :param menu:
    :return:
    """
    if not menu:
        return ''
    html = ''
    for menu_item in menu:
        child = menu_item.get('child', [])
        if child:
            flag = 'active' if menu_item.get('active') is True else ''
            menu_item_html = f'''
            <li class="dropdown {flag}">
                <a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown">
                    {menu_item.get('name')} <span class="caret"></span>
                </a>
                <ul class="dropdown-menu" role="menu" style="left: 0;">
                    {render_top_menu(child)}
                </ul>
            </li>
            '''
        else:
            target_blank = '' if menu_item.get('target_blank') is False else 'target="_blank"'
            flag = 'active' if menu_item.get('active') is True else ''
            menu_item_html = f'''
            <li class="{flag}"><a {target_blank} href="{menu_item.get('url')}"> {menu_item.get('name')}</a></li>
            '''
        html += menu_item_html
    return html


@simple_tag(takes_context=True)
def get_menu(context, request, position: Literal['main', 'top'] = 'main'):
    if not isinstance(request, HttpRequest):
        return None

    # Django 1.9+
    available_apps = context.get('available_apps')
    if not available_apps:

        # Django 1.8 on app index only
        available_apps = context.get('app_list')

        # Django 1.8 on rest of the pages
        if not available_apps:
            try:
                from django.contrib import admin
                template_response = get_admin_site(request.current_app).index(
                    request)
                available_apps = template_response.context_data['app_list']
            except Exception:
                pass
    if not available_apps:
        logging.warn('adminlteui was unable to retrieve apps list for menu.')

    adminlte_config = get_adminlte_config_class()
    if position == 'main':
        menu = adminlte_config.build_main_menu(request, available_apps)
        menu_html = render_main_menu(menu)
    else:
        menu = adminlte_config.build_top_menu(request, available_apps)
        menu_html = render_top_menu(menu)
    return menu_html


def get_admin_site(current_app):
    """
    Method tries to get actual admin.site class, if any custom admin sites
    were used. Couldn't find any other references to actual class other than
    in func_closer dict in index() func returned by resolver.
    """
    try:
        resolver_match = resolve(reverse('%s:index' % current_app))
        # Django 1.9 exposes AdminSite instance directly on view function
        if hasattr(resolver_match.func, 'admin_site'):
            return resolver_match.func.admin_site

        for func_closure in resolver_match.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass
    from django.contrib import admin
    return admin.site
