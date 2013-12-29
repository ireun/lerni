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

@view_config(route_name='install', renderer='install/start.mak')
def install(request):
    page={'editor':False, 'allerts':'', 'banners': [['/static/images/lerni.png','position.alternative']]}
    task1 = task.delay(4,4).id
    time.sleep(1)
    task2 = AsyncResult(task1)
    print task2.result
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