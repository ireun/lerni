# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='successes', renderer='successes.mak')
def succeses(request):
   page={'editor':0, 'breadcrumbs':[["",u"Nasze sukcesy"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['menu_left_list'] =[]
      page['menu_left_list'].append(["/nasze-sukcesy","Wprowadzenie"])
      page['menu_left_list'].append(["/nasze-sukcesy/liceum","Liceum"])
      page['menu_left_list'].append(["/nasze-sukcesy/gimnazjum","Gimnazjum"])
      page['name']=""
      page['title']="Nasze sukcesy"
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page
   
@view_config(route_name='successes_lic', renderer='competitors.mak')
def succeses_lic(request):
   page={'editor':0, 'breadcrumbs':[["/nasze-sukcesy",u"Nasze sukcesy"],["",u"Liceum"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   page['menu_top_list']=menu_top(request)
   page['name']=username(logged_in)
   page['competitors']=[]
   i=0
   try:
      for x in DBSession.query(Competitors).filter_by(competition_group_id=1):
          i+=1
          page['competitors'].append([i,x.first_name+" "+x.last_name,x.competition.name,x.competitor_type.name,x.competitor_tutor.name,str(x.start_year)+"/"+str(x.end_year)])
          
      page['menu_left_list'] =[["/nasze-sukcesy","Wprowadzenie"],["/nasze-sukcesy/liceum","Liceum"],["/nasze-sukcesy/gimnazjum","Gimnazjum"]]
      page['title']="Nasze sukcesy - Liceum"
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page
   
   
@view_config(route_name='successes_gim', renderer='competitors.mak')
def succeses_gim(request):
   page={'editor':0, 'breadcrumbs':[["/nasze-sukcesy",u"Nasze sukcesy"],["",u"Gimnazjum"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   page['menu_top_list']=menu_top(request)
   page['name']=username(logged_in)
   page['competitors']=[]
   i=0
   try:
      for x in DBSession.query(Competitors).filter_by(competition_group_id=2):
          i+=1
          page['competitors'].append([i,x.first_name+" "+x.last_name,x.competition.name,x.competitor_type.name,x.competitor_tutor.name,str(x.start_year)+"/"+str(x.end_year)])
          
      page['menu_left_list'] =[["/nasze-sukcesy","Wprowadzenie"],["/nasze-sukcesy/liceum","Liceum"],["/nasze-sukcesy/gimnazjum","Gimnazjum"]]
      page['title']="Nasze sukcesy - Gimnazjum"
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page

@view_config(route_name='graduates', renderer='graduates.mak')
def graduates(request):
   page={'editor':0, 'breadcrumbs':[["",u"Absolwenci"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['menu_left_list'] =[]
      for position in DBSession.query(MenuLeft):
			page['menu_left_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page

   
@view_config(route_name='companionship', renderer='companionship.mak')
def companionship(request):
   page={'editor':0, 'breadcrumbs':[["",u"Towrzystwo Szkół Twórczych"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['menu_left_list'] =[]
      for position in DBSession.query(MenuLeft):
			page['menu_left_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page

@view_config(route_name='contact', renderer='contact.mak')
def contact(request):
   page={'editor':0, 'breadcrumbs':[["",u"Towrzystwo Szkół Twórczych"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['menu_left_list'] =[]
      for position in DBSession.query(MenuLeft):
			page['menu_left_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page
   
@view_config(route_name='books', renderer='books.mak')
def books(request):
   page={'editor':0, 'breadcrumbs':[["",u"Podręczniki"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['menu_left_list'] =[]
      for position in DBSession.query(MenuLeft):
			page['menu_left_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page

@view_config(route_name='competitions', renderer='competitions.mak')
def competitions(request):
   page={'editor':0, 'breadcrumbs':[["",u"Konkursy"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['menu_left_list'] =[]
      for position in DBSession.query(MenuLeft):
			page['menu_left_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
         
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page
   
@view_config(route_name='connection')
def competitions(request):
    username = request.params['username'] + request.params['n1a'] + request.params['n2a'] + request.params['n3a'] + request.params['n4a'] + request.params['n1b'] + request.params['n2b'] + request.params['n3b'] + request.params['n4b'] + request.params['n1c'] + request.params['n2c'] + request.params['n3c'] + request.params['n4c'] + request.params['n1d'] + request.params['n2d'] + request.params['n3d'] + request.params['n4d'] + request.params['n1e'] + request.params['n2e'] + request.params['n3e'] + request.params['n4e'] + request.params['n1f'] + request.params['n2f'] + request.params['n3f'] + request.params['n4f']
    print(username)
    response = Response(body='10', content_type='text/plain')
    return response

@view_config(route_name='view_page', renderer='pages.mak')
def view_page(request):
    pagename = request.matchdict['pagename']
    Page = DBSession.query(Pages).filter_by(url_name=pagename).first()
    if Page is None:     
        page={'editor':0, 'allerts':[]}
        logged_in = authenticated_userid(request)
        page['logged_in']=logged_in
        Page = DBSession.query(Pages).filter_by(url_name="main_page").first()
        SubPage = DBSession.query(SubPages).filter_by(page_id=Page.id).filter_by(url_name=request.matchdict['pagename']).first()
        if SubPage is None:
            return HTTPNotFound('No such page')
        page['data']=SubPage.data
        page['breadcrumbs']=[["",SubPage.name]]
        if Page is None:
            return HTTPNotFound('No such page')
        try:
            page['menu_top_list']=[]
            for position in DBSession.query(MenuTop):
                page['menu_top_list'].append([position.link,position.name])
            page['menu_left_list'] =[['/',u'Strona Główna']]
            for position in Page.sub_pages:
                page['menu_left_list'].append(["/p/"+position.url_name,position.name])
            page['name']=""
            if logged_in:
                page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
        except DBAPIError:
            return Response("Mysql connection error", content_type='text/plain', status_int=500)
        return page
    SubPage = DBSession.query(SubPages).filter_by(page_id=Page.id).first() ## Add Sorting
    if SubPage is None:
        return HTTPNotFound('No such page')
    return HTTPFound(location = request.route_url('page', pagename = Page.url_name, subname = SubPage.url_name))

@view_config(route_name='page', renderer='pages.mak')
def page(request):
    page={'editor':0, 'allerts':[]}
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    pagename = request.matchdict['pagename']
    Page = DBSession.query(Pages).filter_by(url_name=pagename).first()
    SubPage = DBSession.query(SubPages).filter_by(page_id=Page.id).filter_by(url_name=request.matchdict['subname']).first()
    page['data']=SubPage.data
    page['breadcrumbs']=[["/p/"+Page.url_name,Page.name],["",SubPage.name]]
    if Page is None:
        return HTTPNotFound('No such page')
    page['menu_left_list'] =[]
    for position in Page.sub_pages:
        page['menu_left_list'].append(["/p/"+Page.url_name+"/"+position.url_name,position.name])        
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)        
    return page

@view_config(route_name='gallery', renderer='gallery.mak')
def gallery(request):
    page={'editor':0, 'allerts':[]}
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in

    page['breadcrumbs']=[["","Galeria"]]
    page['menu_left_list'] =[]
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    return page




