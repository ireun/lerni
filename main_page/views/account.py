# -*- coding: utf-8 -*-
from base import *
import hashlib
import random
@view_config(route_name='account', renderer='account.mak')
def account_base(request):
   menu_left_list=[[request.route_url('account'),"Edytuj profil"],[request.route_url('phone_app'),u"Powiadomienia"]]
   menu_left_list+=[[request.route_url('phone_app'),u"Powiązane konta"],[request.route_url('phone_app'),u"Aplikacja na telefon"],
   [request.route_url('logout'),u"Wyloguj"]]
   page={'editor':0, 'breadcrumbs':[["","Ustawienia"],["","Edytuj profil"]], 'menu_left_list':menu_left_list, 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
         page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
         page['first_name']=DBSession.query(People).filter_by(login=logged_in).first().first_name
         page['second_name']=DBSession.query(People).filter_by(login=logged_in).first().second_name
         page['last_name']=DBSession.query(People).filter_by(login=logged_in).first().last_name
         pesel=DBSession.query(People).filter_by(login=logged_in).first().pesel
         century=["19","20","21","22","18"][int(pesel[2:4])/20]
         birthday_passed=datetime.date(2000,datetime.datetime.today().month,datetime.datetime.today().day)<datetime.date(2000,int(pesel[2:4]),int(pesel[4:6]))
         page['years']=datetime.datetime.today().year-datetime.date(int(century+pesel[:2]),int(pesel[2:4]),int(pesel[4:6])).year-birthday_passed
         page['gender']=[u"Kobieta",u"Mężczyzna"][int(pesel[9])%2]
         page['group']="Todo"#klasa + grupa
         page['language_group']="Todo"#lektorat + grupa
         page['extension_group']="Todo"#rozszerzenie
      else:
      	return Response("User not logged in", content_type='text/plain', status_int=500) #dodać redirecta na stronę logowania
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page
@view_config(route_name='phone_app', renderer='phone_app.mak')
def account_phone_app(request):
   menu_left_list=[[request.route_url('account'),"Edytuj profil"],[request.route_url('phone_app'),u"Powiadomienia"]]
   menu_left_list+=[[request.route_url('phone_app'),u"Powiązane konta"],[request.route_url('phone_app'),u"Aplikacja na telefon"],
   [request.route_url('logout'),u"Wyloguj"]]
   page={'editor':0, 'breadcrumbs':[["","Ustawienia"],["","Aplikacja na telefon"]], 'menu_left_list':menu_left_list, 'allerts':[]}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   try:
      page['menu_top_list']=[]
      for position in DBSession.query(MenuTop):
         page['menu_top_list'].append([position.link,position.name])
      page['name']=""
      if logged_in:
      	page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
      	user_id=DBSession.query(People).filter_by(login=logged_in).first().id
      	if 'action' in request.params:
      		if request.params['action']=="add_phone":
      			if	int(DBSession.query(AppCodes).filter_by(user_id=user_id).count())>9:
      				page["allerts"].append([u"Limit podłączonych urządzeń (10) został osiągnięty.","error","topRight"])
      			elif int(DBSession.query(AppCodes).filter_by(user_id=user_id).filter_by(phone_id="phone_id").count())>0:
      				page["allerts"].append([u"Wykorzystaj wygenerowany kod QR do podłączenia urządzenia, a następnie wygeneruj kolejny.","allert","topRight"])
      			else:
	      			with transaction.manager:
							model = AppCodes(user_id, "phone_name", "phone_id", hashlib.sha224(str(random.random())).hexdigest())
							DBSession.add(model)	
      		elif request.params['action']=="delete":
					if 'code' in request.params:
						with transaction.manager:
							DBSession.query(AppCodes).filter_by(code=request.params['code']).delete()  #${request.application_url}
      	page['phones']=[]
      	for position in DBSession.query(AppCodes).filter_by(user_id=user_id):
      		page['phones'].append([position.phone_name,position.code,position.phone_id]) #position.user.username
      else:
      	return Response("User not logged in", content_type='text/plain', status_int=500) #dodać redirecta na stronę logowania
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page