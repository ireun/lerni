# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='install', renderer='install/start.mak')
def install(request):
    page={'editor':False, 'allerts':'', 'banners': [['/static/images/lerni.png','position.alternative']]}
    return page