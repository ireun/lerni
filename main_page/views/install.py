# -*- coding: utf-8 -*-
from main_page.views.base import *
import os
import sys
import transaction
import datetime
import yaml

import csv #####################################
from sqlalchemy import Table ###################
from sqlalchemy import engine_from_config

from os import listdir
from os.path import isfile, join
import codecs
from celery.result import AsyncResult

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from main_page.tasks import task
import urllib2
import celery
@view_config(route_name='install', renderer='install/start.mak')
def install(request):
    page={'editor': False, 'allerts': '', 'banners': [['/static/images/lerni.png', 'Lerni Logo']]}
    page['page_title'] = "Lerni - instalacja"  #ZSO nr 15 w Sosnowcu
    page['internet_on'] = internet_on()
    try:
        page['celery'] = 8 == task.delay(4,4).wait(timeout=2, propagate=True, interval=0.5)
    except celery.exceptions.TimeoutError:
        page['celery'] = False
    try:
        gnupg.GPG(gnupghome='GPG')
        page['gpg'] = True
    except ValueError:
        page['gpg'] = False
    page['update_available'] = False
    #time.sleep(1)
    #task2 = AsyncResult(task1)
    #print task2.result
    if False:
        config_uri = "development.ini"
        setup_logging(config_uri)
        settings = get_appsettings(config_uri)
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
    return page

#@view_config(route_name='install', renderer='install/start.mak')
#def install(request):
#    page={'editor':False, 'allerts':'', 'banners': [['/static/images/lerni.png','position.alternative']]}
#    return page

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False