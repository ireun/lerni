# -*- coding: utf-8 -*-
from base import *
#@forbidden_view_config(renderer='login.mak')
@view_config(route_name='login', renderer='login.mak')
def login(request):
   page={'editor':0, 'breadcrumbs':[["",u"Nasze sukcesy"]], 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=menu_top(request)
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   login_url = request.route_url('login')
   referrer = request.url
   if referrer == login_url:
      referrer = '/' # never use the login form itself as came_from
   came_from = request.params.get('came_from', referrer)
   if 'login' in request.params and 'password' in request.params:
      login = request.params['login']
      password = request.params['password']
      try:
         correct_password=DBSession.query(People).filter_by(login=login).first().password
      except AttributeError:
         page['allerts'].append([u"Zła nazwa użytkownika bądź hasło","information","topRight"])
         return page
      if correct_password == password:
         headers = remember(request, login)
         response = HTTPFound(location = request.route_url('home'))
         response.headerlist.extend(headers)
         return response
      page['allerts'].append([u"Zła nazwa użytkownika bądź hasło","information","topRight"])
      return response
   return page