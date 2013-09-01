# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='login', renderer='login.mak')  ## Dodać "Aby zobaczyć tą stronę musisz się zalogować"###
def login(request):
	page={'editor':0, 'allerts':[], 'recaptcha_public':recaptcha_public, 'active':'login'}
	next = request.referer or request.url
	if next == request.route_url('login'):
		next = request.route_url('home')
	login = ''
	logged_in = authenticated_userid(request)
	page['logged_in']=logged_in
	page['name']=username(logged_in)
	if logged_in: return HTTPFound(location = next)
	if set(['login','password']) <= set(request.params):
		login = request.POST.get('login', '')
		passwd = request.POST.get('password', '')
		session = DBSession()
		user = DBSession.query(People).filter_by(email=login).first()
		if user and user.check_password(passwd):
			if 'remember_me' in request.params:
				headers = remember(request, login, max_age=60*60*24*7)
			else:
				headers = remember(request, login)
			user.last_login=datetime.datetime.now()
			session.add(AALogin(user.id,request.client_addr,request.user_agent,str(request.accept_language),datetime.datetime.now()))
			transaction.commit()
			return HTTPFound(location=next, headers=headers)
		page['allerts'].append([u"Zła nazwa użytkownika bądź hasło","information","topRight"])
	return page
			
			
@view_config(route_name='logout')
def logout(request):
	next = request.params.get('next') or request.route_url('home')
	headers = forget(request)
	return HTTPFound(location = next,headers = headers)