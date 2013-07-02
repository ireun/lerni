# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('view_home'),
                     headers = headers)