# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

import transaction
import datetime
import linecache

from sqlalchemy.exc import DBAPIError
import locale
from sqlalchemy import desc    ######################################
from main_page.models import (
    DBSession,
    MenuTop,
    MenuLeft,
    Articles,
    ArticlesContent,
    Articles_Comments,
    Users_Groups,
    Base,
    Substitutions,
    Occupations,
    Titles,
    People,
    Absent,
    Replace,
    Duty,
    Shift,
    Places,
    Subjects,
    Schedules,
    LuckyNumbers,
    SchoolYears,
    Groups,
    Lessons,
    Association,
    SupportSections,
    SupportSubSections,
    SupportTickets,
    SupportQuestions,
    AppCodes,
    Pages,
    SubPages,
    Competitors,
    CompetitorsCompetitions,
    CompetitorsTutors,
    CompetitorsTypes,
    CompetitorsGroups,
    Files
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
   
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

def menu_left(request):
   menu_left_list=[[request.route_url('support'),"Centrum Supportu"],[request.route_url('support_services'),u"Status serwisów"]]
   menu_left_list+=[[request.route_url('support_stats'),u"Statystyki"],[request.route_url('support_ask'),u"Zapytaj"]]
   menu_left_list+=[[request.route_url('support_faq'),u"FAQ"]]
   return menu_left_list
def menu_top(request):
   try:
      menu_top_list=[]
      for position in DBSession.query(MenuTop):
         menu_top_list.append([position.link,position.name])
      return menu_top_list
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
def username(logged_in):
   try:
      name=""
      if logged_in:
         name=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return name

