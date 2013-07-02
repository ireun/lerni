# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

import transaction
import datetime

from sqlalchemy.exc import DBAPIError
import locale
from sqlalchemy import desc    ######################################
from main_page.models import (
    DBSession,
    MenuTop,
    MenuLeft,
    Articles,
    Articles_Comments,
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
    exception_response,
    )    
    
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    has_permission,
    )

from pyramid.security import authenticated_userid
from math import ceil

@view_config(route_name='add_comment')
def login(request):
   if 1:
      article_id = request.params['id']
      content = request.params['content']
      login = authenticated_userid(request)
      user_id = DBSession.query(People).filter_by(login=login).first().id
      with transaction.manager:
         DBSession.add_all([
            Articles_Comments(article_id,datetime.datetime.now(),user_id,content)
         ])
      response = Response(body='OK', content_type='text/plain')
      return response
   response = Response(body='FAIL', content_type='text/plain')
   return response
   
@view_config(route_name='rm_comment')
def login2(request):
   if 1:
      comment_id = request.params['comment_id']   ############ Check permissions here!
      #user_id = DBSession.query(Users).filter_by(login=login).first().id      
      DBSession.delete(DBSession.query(Articles_Comments).filter_by(id=comment_id).first())
      response = Response(body='OK', content_type='text/plain')
      return response
   response = Response(body='FAIL', content_type='text/plain')
   return response