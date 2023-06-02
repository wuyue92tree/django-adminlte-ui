from typing import Literal, List


class MenuItem(object):
    def __init__(self, label: str, name: str = None, url=None,
                 icon: str = 'fa-circle-o',
                 menu_type: Literal['group', 'model', 'link'] = 'group',
                 child: List = None, target_blank: bool = False,
                 permissions: List = None):
        self.name = name
        self.label = label
        self.url = url
        self.icon = icon
        self.menu_type = menu_type
        self.child = child
        self.target_blank = target_blank
        self.permissions = permissions

    def make(self, request, models=None, deep=1, deep_limit=0):
        menu_item = {'name': self.name, 'icon': self.icon, 'label': self.label}
        if self.child and self.menu_type != 'group':
            raise Exception(
                'menu_type must setup to group when child is not None.')

        if self.menu_type == 'model':
            if models is None:
                raise Exception('models must setup when menu_type="model".')
            if self.label not in models.keys():
                raise Exception(f'got an invalid label for model: {self.label}')
            model = models.get(self.label)
            if not self.name:
                menu_item['name'] = model.get('name')
            menu_item['url'] = model.get('admin_url')
        elif self.menu_type == 'link':
            menu_item['url'] = self.url
        else:
            # menu_type: group and child is empty will hide the menu
            if not self.child:
                return None

        if menu_item.get('name') is None:
            # setup name as label when name is None
            menu_item['name'] = menu_item['label']

        menu_item['target_blank'] = self.target_blank

        if self.child:
            if deep_limit == 0 or deep <= deep_limit:
                child_list = []
                for child in self.child:
                    deep += 1
                    child_menu = child.make(request, models, deep, deep_limit)
                    if child_menu:
                        child_list.append(child_menu)
                menu_item['child'] = child_list
            else:
                return None
        return menu_item


class AdminLteConfig(object):
    main_menu = []
    top_menu = []
    show_avatar = False
    avatar_field = None
    username_field = None

    site_logo = None

    skin = None

    search_form = True
    copyright = None
    welcome_sign = None

    @staticmethod
    def get_models(app_list):
        models = {}
        for app in app_list:
            for model in app.get('models', []):
                models[
                    f'{app.get("app_label")}.' \
                    f'{model.get("object_name")}'] = model
        return models

    def build_main_menu(self, request, app_list):
        if not self.main_menu:
            # if main_menu is not setup, fill the app_list
            for app in app_list:
                menu_item = MenuItem(
                    label=app.get('app_label'), name=app.get('name'), child=[
                        MenuItem(
                            label=f'{app.get("app_label")}.'
                                  f'{model.get("object_name")}',
                            menu_type='model') for model in
                        app.get('models')
                    ])
                self.main_menu.append(menu_item)

        menu = []
        models = self.get_models(app_list)
        for menu_item in self.main_menu:
            menu_item_ = menu_item.make(request, models)
            if menu_item_:
                menu.append(menu_item_)
        return menu

    def build_top_menu(self, request, app_list):
        """
        top menu deep_limit force to 2
        :param request:
        :param app_list:
        :return:
        """
        if not self.top_menu:
            # if main_menu is not setup, keep empty
            return []
        menu = []
        models = self.get_models(app_list)
        for menu_item in self.top_menu:
            menu_item_ = menu_item.make(request, models, deep_limit=2)
            if menu_item_:
                menu.append(menu_item_)
        return menu
