#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2017-03-01
# @Author  : wangpeng
# @Desc	   : clear all app migrations
from travel.wsgi import *
import os

if __name__ == '__main__':
    from django.apps import apps

    i_apps = apps.get_app_configs()
    for app in i_apps:
        app_path = getattr(app, 'path')
        app_name = getattr(app, 'label')
        migration_path = os.path.join(app_path, 'migrations')
        c_path = os.getcwd()
        if os.path.exists(migration_path) and migration_path.find(c_path)>-1:
            for f_name in os.listdir(migration_path):
                if f_name != '__init__.py':
                    os.remove(os.path.join(migration_path,f_name))