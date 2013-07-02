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

import random
import md5
import string
###################################################
##   REGISTER FORM      ###########################
###################################################

@view_config(route_name='register', renderer='register.mak')
def my_view(request):
    logged_in = authenticated_userid(request)
    try:
       menu_top_list =[]
       for position in DBSession.query(MenuTop):
       	menu_top_list.append([position.link,position.name])
       menu_left_list =[]
       for position in DBSession.query(MenuLeft):
       	menu_left_list.append([position.link,position.name])
       articles =[]
       for position in DBSession.query(Articles):
       	username = DBSession.query(People).filter_by(id=position.author_id).first().username
       	articles.append([position.title,str(position.add_date)[:str(position.add_date).find(".")],username,position.content])
       	
       rs=''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(15))
       i=["mg","na","dv","aw","sa"]
       random.shuffle(i)
       i.append(i[random.randint(0,4)])
       m=md5.md5(rs[:4]+i[0]+rs[4:6]+i[1]+rs[6:9]+i[2]+rs[9:10]+i[3]+rs[10:12]+i[4]+rs[12:15]+i[5])
       text = m.hexdigest()
       names = {"mg":"banana","na":"jablko","dv":"slonia","aw":"krowe","sa":"lolface"}
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'menu_top_list':menu_top_list, 'menu_left_list':menu_left_list, 'articles':articles, 'logged_in':logged_in,
    'captcha':rs[:4]+rs[4:6]+rs[6:9]+rs[9:10]+rs[10:12]+rs[12:15]+text, 'quest':names[i[5]]}
    
    
#####################################################
# CAPTCHA ###########################################
#####################################################
@view_config(route_name='captcha')
def add_page(request):
    hc = request.matchdict['hashcode']  #### MOZNA LADNIEJ, NIE CHCE MI SIE
    str_to_return="none"
    for a in ["mg","na","dv","aw","sa"]:
        for b in ["mg","na","dv","aw","sa"]:
            for c in ["mg","na","dv","aw","sa"]:
                for d in ["mg","na","dv","aw","sa"]:
                    for e in ["mg","na","dv","aw","sa"]:
                        for f in ["mg","na","dv","aw","sa"]:
                            m=md5.md5(hc[:4]+a+hc[4:6]+b+hc[6:9]+c+hc[9:10]+d+hc[10:12]+e+hc[12:15]+f)
                            if m.hexdigest() == hc[15:]:
                                str_to_return=a+b+c+d+e
    response = Response(content_type='image/jpeg')
    response.app_iter = open('./main_page/captcha/done/'+str_to_return+'.png', 'rb')
    return response
#####################################################
## CAPTCHA VALIDATE 
@view_config(route_name='captcha_validate')
def validate(request):
    hc = request.matchdict['hashcode']  #### MOZNA LADNIEJ, NIE CHCE MI SIE
    str_to_return="none"
    ids = {"mg":"1","na":"2","dv":"3","aw":"4","sa":"5"}
    for a in ["mg","na","dv","aw","sa"]:
        for b in ["mg","na","dv","aw","sa"]:
            for c in ["mg","na","dv","aw","sa"]:
                for d in ["mg","na","dv","aw","sa"]:
                    for e in ["mg","na","dv","aw","sa"]:
                        for f in ["mg","na","dv","aw","sa"]:
                            m=md5.md5(hc[1:5]+a+hc[5:7]+b+hc[7:10]+c+hc[10:11]+d+hc[11:13]+e+hc[13:16]+f)
                            ids2 = {"1_":ids[a],"2_":ids[b],"3_":ids[c],"4_":ids[d],"5_":ids[e]}
                            if m.hexdigest() == hc[16:]:
                                if ids[f] == ids2[str(str(hc[0])+"_")]:
                                    str_to_return="OK"
                                else:
                                    str_to_return="WRONG"
    response = Response(body=str_to_return, content_type='text/plain')
    return response