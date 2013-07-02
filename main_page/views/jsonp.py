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
    Association
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

@view_config(route_name='jsonp_post_comments', renderer='jsonp')
def my_view(request):
    article_id = int(request.GET['post_id'])
    comments=[]
    for position in DBSession.query(Articles_Comments).filter_by(article_id=article_id):
       username=DBSession.query(People).filter_by(id=position.author_id).first().username
       comments.append([position.id,username,str(position.add_date)[:str(position.add_date).find(".")],position.content])
    return {'comments':comments}

@view_config(route_name='jsonp_people', renderer='jsonp')
def my_view2(request):
    #article_id = int(request.GET['post_id'])
    people=[]
    for position in DBSession.query(People):
       people.append([position.id,position.first_name,position.last_name])
       #username=DBSession.query(People).filter_by(id=position.author_id).first().username
       #comments.append([position.id,username,str(position.add_date)[:str(position.add_date).find(".")],position.content])
    return {'people':people}

@view_config(route_name='jsonp_groups', renderer='jsonp')
def my_view3(request):
    groups=[]
    for position in DBSession.query(Groups):
       groups.append(position.name)
    return {'groups':groups}


@view_config(route_name='jsonp_mobile_login', renderer='jsonp')
def my_view4(request):
    #code = request.POST['code']
    code="UKJAASDLXCAOIW3245"
    username=[]
    groups=[]
    lessons=["","","","","","",""]
    for position in DBSession.query(People).filter_by(app_code=code):
       username.append(position.username)
       for lol in position.classes:
          for xd in DBSession.query(Groups).filter_by(id=lol.groups_id):
             groups.append(xd.name)
          for woow in DBSession.query(Lessons).filter_by(group_id=lol.groups_id).filter_by(day=1).filter_by(part_1=lol.part_1):
             lessons[int(woow.order)-1]=unicode(woow.order)+u". "+unicode(woow.teacher_subject.subject.name)+u" "+unicode(woow.teacher_subject.teacher.username)
    return {'username':username,'groups':groups,'lessons':lessons}







