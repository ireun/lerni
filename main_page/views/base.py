# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

import transaction
import datetime
import time
import linecache
import uuid
import hashlib

from recaptcha.client import captcha

from sqlalchemy.exc import DBAPIError
import locale
from sqlalchemy import desc    ######################################
from main_page.models import (
    DBSession,
    MenuTop,
    MenuLeft,
    Base,
    Substitutions,
    People,
    AALogin,
    Wallet,   
	 
    Folders,
    FoldersVersions,
    FoldersCSS,
    FoldersCSSVersions,
    FoldersTags,
    Entries,
    EntriesVersions,
    EntriesCSS,
    EntriesCSSVersions,
    EntriesLikes,
    EntriesTags,
    Tags,
    Tweets,
    TweetsMain,
    Videos,
    VideosMain,
    Banners,
    Sets,
    SetsItems,
    EasyLinks,


    Teachers,
    Students,
    Absent,
    Replace,
    Duty,
    Shift,
    Places,
    Subjects,
    Schedules,
    LuckyNumbers,
    SchoolYears,
    DivisionsCategories,
    Divisions,
    Groups,
    Lessons,
    LessonsGroups,
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

from itsdangerous import URLSafeSerializer
secret = 'secret-key'
recaptcha_private = "6Lfz3OUSAAAAANh7eynb6CW4aehuKxK6yLgnPRg8"
recaptcha_public = "6Lfz3OUSAAAAACtP35cn21roRF4k9eS5Tw6c6ik2"
import os
import gnupg
from pprint import pprint
gpg = gnupg.GPG(gnupghome='GPG')


from BeautifulSoup import BeautifulSoup
import json
import pdfkit
from pyramid.renderers import render
import tempfile
from contextlib import contextmanager
import string
valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

@contextmanager
def tempinput(data):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    temp.write(data.encode('utf8'))
    temp.close()
    yield temp.name
    os.unlink(temp.name)
    
def pl_to_ascii(tekst):
    pl = {ord(u'Ą'): u'A',ord(u'Ć'): u'C',ord(u'Ę'): u'E',ord(u'Ł'): u'L',ord(u'Ó'): u'O',ord(u'Ś'): u'S',ord(u'Ź'): u'Z',ord(u'Ż'): u'Z',
    		ord(u'ą'): u'a',ord(u'ć'): u'c',ord(u'ę'): u'e',ord(u'ł'): u'l',ord(u'ó'): u'o',ord(u'ś'): u's',ord(u'ź'): u'z',ord(u'ż'): u'z'}
    return tekst.translate(pl)
def response_pdf(request,html,filename):
    response = request.response
    with tempinput(html) as tempfilename:
        with tempinput("") as output_file:
            wk=WKhtmlToPdf(tempfilename,output_file,dpi="300",screen_resolution=[1280, 1024])
            response.body_file=pdfkit.from_file('test.html', False)
            response.content_type = 'application/pdf'
            filename=(filename).replace(" ","_")
            filename=pl_to_ascii(filename)
            filename=''.join(c for c in filename if c in valid_chars).strip(".")
            response.headerlist.append(("Content-Disposition", "attachment; filename='"+str(filename)+".pdf'"))
            return response
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
         name=DBSession.query(People).filter_by(email=logged_in).first().first_name
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return name
   
from string import digits
from random import choice
def new_pin():
	return ''.join(choice(digits) for i in xrange(4))

def send_mail(request,subject,recipients,body,fingerprint=False):
	if fingerprint:
		body=str(gpg.encrypt(body, fingerprint, always_trust=True))
	mailer = request.registry['mailer']  
	message = Message(subject=subject,
	                  sender="mailer.staszic@gmail.com",
	                  recipients=recipients,
	                  body=body)
	mailer.send_immediately(message)
	
import bbcode

parser = bbcode.Parser(normalize_newlines=False, install_defaults=False, escape_html=False, replace_links=False, replace_cosmetic=False)
parser.add_simple_formatter('hr', '<hr />', standalone=True)
parser.add_simple_formatter('p', '<p>%(value)s</p>')
parser.add_simple_formatter('diagram', '<div class="diagram">%(value)s</div>')
parser.add_simple_formatter('date','<abbr class="timeago" title="%(value)s">%(value)s</abbr>')


# A custom render function.
def render_color(tag_name, value, options, parent, context):
    return '<span style="color:%s;">%s</span>' % (tag_name, value)

# Installing advanced formatters.
for color in ('red', 'blue', 'green', 'yellow', 'black', 'white'):
    parser.add_formatter(color, render_color)


def get_basic_account_info():
    page={}
    page['balance_history'] = ",".join(["0","0","0","0","0","0","0","0","0"])
    page['balance']=0
    page['likes_history'] = ",".join(["0","0","0","0","0","0","0","0","0"])
    page['likes']=0
    page['subscribers_history'] = ",".join(["0","0","0","0","0","0","0","0","0"])
    page['subscribers']=0
    page['preparation_history'] = ",".join(["100","100","100","100","100","100","100","100","100"])
    page['preparation']=100
    return page




