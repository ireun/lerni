# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
import locale
from sqlalchemy import desc    ######################################
from main_page.models import (
    DBSession,
    MenuTop,
    MenuLeft,
    Articles,
    Substitutions,
    Absent,
    Replace,
    People,
    Lessons,
    Groups,
    Duty,
    Shift,
    Places,
    )
#import re
#from docutils.core import publish_parts
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )        
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )
from pyramid.security import authenticated_userid

#@forbidden_view_config(renderer='login.mak')
@view_config(route_name='login', renderer='login.mak')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        try:
            correct_password=DBSession.query(People).filter_by(login=login).first().password
        except AttributeError:
            response = Response(body='Wrong username or password', content_type='text/plain')
            return response
        if correct_password == password:
            headers = remember(request, login)
            response = Response(body='OK', content_type='text/plain')
            response.headerlist.extend(headers)
            return response
        response = Response(body='Wrong username or password', content_type='text/plain')
        return response
    response = []
    return response
    
    
    
    