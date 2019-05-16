#coding:utf8

from django.apps import AppConfig

import os
import pymysql
pymysql.install_as_MySQLdb()

default_app_config = 'trainsite.axlepress'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class AxlePress(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = "车轴受力测量"