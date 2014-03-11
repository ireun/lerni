# -*- coding: utf-8 -*-
from base import *
import hashlib
import random
@view_config(route_name='account', renderer='account.mak', permission='account_settings')
def account_base(request):
   page={'editor':0, 'allerts':[]}
   logged_in = authenticated_userid(request)
   try:
   	user = DBSession.query(People).filter_by(email=logged_in).first()
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   page['logged_in']=logged_in       ## Not really important
   page['name']=username(logged_in)  ##
   page.update({'first_name':user.first_name,'second_name':user.second_name,'last_name':user.last_name,
   'pesel':user.pesel,'birthdate':str(user.birthdate),'gender':[u"Kobieta",u"Mężczyzna"][user.is_male],
   'group':"todo",'language_group':"todo",'extension_group':"todo"})
   return page
@view_config(route_name='phone_app', renderer='phone_app.mak')
def account_phone_app(request):
   page={'editor':0, 'allerts':[]}
   logged_in = authenticated_userid(request)
   try:
   	user = DBSession.query(People).filter_by(email=logged_in).first()
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
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


@view_config(route_name='account_folders', renderer='admin_jtable.mak')
def account_folders(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["",u"Moje konto"],["",u"Foldery"]], 'allerts':[]}
    page.update(get_basic_account_info(request))
    logged_in = authenticated_userid(request)
    page['name']=username(logged_in)
    page['title']=u"Foldery"
    page['title_desc']= u"Stwórz folder w którym będziesz umieszczać swoje wpisy.\
                        Możesz utworzyć więcej niż jeden folder."
    page['table_name']="table_folders"
    return page

@view_config(route_name='account_entries', renderer='admin_jtable.mak')
def account_entries(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["",u"Moje konto"],["",u"Wpisy"]], 'allerts':[]}
    page.update(get_basic_account_info(request))
    logged_in = authenticated_userid(request)
    page['name']=username(logged_in)
    page['title']=u"Wpisy"
    page['title_desc']= u"Poniżej możesz utworzyć nowy wpis."
    page['table_name']="table_entries"
    return page

@view_config(route_name='account_presentations', renderer='admin_jtable.mak')
def account_presentations(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["",u"Moje konto"],["",u"Prezentacje"]], 'allerts':[]}
    page.update(get_basic_account_info(request))
    logged_in = authenticated_userid(request)
    page['name']=username(logged_in)
    page['title']=u"Prezentacje"
    page['title_desc']= u"Poniżej możesz utworzyć nową prezentację."
    page['table_name']="table_folders"
    return page

@view_config(route_name='account_tasks_sets', renderer='admin_jtable.mak')
def account_tasks_sets(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["",u"Moje konto"],["",u"Foldery"]], 'allerts':[]}
    page.update(get_basic_account_info(request))
    logged_in = authenticated_userid(request)
    page['name']=username(logged_in)
    page['title']=u"Zestawy zadań"
    page['title_desc']= u"Tutaj możesz utworzyć zestaw zadań (not done yet)"
    page['table_name']="table_folders"
    return page

#@view_config(route_name='account_competitions', renderer='admin_jtable.mak')
#def account_tasks_sets(request):
#    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["",u"Moje konto"],["",u"Konkursy"]], 'allerts':[]}
#    page.update(get_basic_account_info(request))
#    logged_in = authenticated_userid(request)
#    page['name']=username(logged_in)
#    page['title']=u"Foldery"
#    page['title_desc']= u"Tutaj możesz utworzyć stronę konkursu (not done yet)"
#    page['table_name']="table_folders"
#    return page