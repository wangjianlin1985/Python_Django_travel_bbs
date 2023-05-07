# -*- coding: utf-8 -*-
from travel.wsgi import *

if __name__ == '__main__':
    from django.apps import apps

    i_apps = apps.get_app_configs()
    for app in i_apps:
        app_path = getattr(app, 'path')
        app_name = getattr(app, 'label')
        f_record_path = os.path.join(app_path, 'create_records.py')
        if os.path.exists(f_record_path):
            app_module = __import__(app_name + '.create_records')
            cr = getattr(app_module, 'create_records')
            cr.make_data()
