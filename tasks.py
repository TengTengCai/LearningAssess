import configparser
import os

import MySQLdb
from invoke import task

BASE_CONFIG = configparser.ConfigParser()
BASE_CONFIG.read('config.ini')
MYSQL_SETTINGS = BASE_CONFIG['MYSQL_SETTINGS']
REDIS_SETTINGS = BASE_CONFIG['MYSQL_SETTINGS']


@task
def build(c):
    print("Building!")


@task
def create_db(c):
    conn = MySQLdb.connect(
        host=MYSQL_SETTINGS['host'],
        port=int(MYSQL_SETTINGS['port']),
        user=MYSQL_SETTINGS['user'],
        passwd=MYSQL_SETTINGS['passwd'],
    )
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_SETTINGS['db']};")


@task
def init_db(c):
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningAssess.settings')
    django.setup()
    from apps.config.models import Config

    if Config.objects.all().count() == 0:
        Config(
            xetong_address='http://example.com',
            shop_address='http://example.com'
        ).save()
