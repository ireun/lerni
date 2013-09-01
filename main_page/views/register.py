# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='register', renderer='login.mak')
def register(request):
   page={'editor':0, 'allerts':[], 'recaptcha_public':recaptcha_public, 'active':'register'}
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in   
   page['name']=username(logged_in)
   page.update({'css_url':request.webassets_env['r_css'].urls()[0],'js_url':request.webassets_env['r_js'].urls()[0],'libs_url':request.webassets_env['libs_js'].urls()[0]}) 
   if logged_in: return HTTPFound(location = request.route_url('home'))

   if set(['recaptcha_challenge_field','recaptcha_response_field2','name','secondname','surname',
   'pesel','birthdate','phonenumber','email','password','repeat-password','gpg']) <= set(request.params):
	   response = captcha.submit(request.params['recaptcha_challenge_field'],request.params['recaptcha_response_field2'],recaptcha_private,request.remote_addr)
	   try:
	   	input_file = request.POST['gpg'].file
	   	key_data = input_file.read()
	   	import_result = gpg.import_keys(key_data)
	   	fingerprint = import_result.results[0]['fingerprint']
	   	use_gpg=1
	   except AttributeError:
	   	use_gpg=0
	   if use_gpg and not 'ok' in import_result.results[0]:
	   	page['allerts'].append([u"Import klucza publicznego zakończony niepowodzeniem.","information","topRight"])	
	   elif request.params['name'] == "" or request.params['surname']=="":
	   	page['allerts'].append([u"Zapomniałeś podać swojego imienia bądź nazwiska.","information","topRight"])
	   elif not is_pesel_correct(request.params['pesel']):
	   	page['allerts'].append([u"Numer pesel nie jest poprawny.","information","topRight"])	
	   elif not is_date_correct(request.params['birthdate']):
	  		page['allerts'].append([u"Podana data urodzenia jest nieprawidłowa.","information","topRight"])
	   elif request.params['password'] != request.params['repeat-password']:
			page['allerts'].append([u"Podane hasła nie są takie same.","information","topRight"])
	   elif len(request.params['password'])<6:
			page['allerts'].append([u"Hasło zbyt krótkie. Aby hasło było bezpiecznie musi składać się z przynajmniej sześciu znaków.","information","topRight"])
	   elif not True:#response.is_valid:
			page['allerts'].append([u"Captcha incorrect","information","topRight"])
	   else:
	   	session = DBSession(expire_on_commit=False)
   		wallet=Wallet(0)
   		session.add(wallet)
   		transaction.commit()		##Warto zrobić jakoś ładnie
   		session2=DBSession()
   		user = People(request.params['name'],request.params['secondname'],request.params['surname'],
   		request.params['pesel'],datetime.datetime.strptime(request.params['birthdate'], '%d/%m/%Y').date(),
   		request.params['phonenumber'],request.params['email'],request.params['password'],
   		key_data,fingerprint,wallet.id,0,0,0,0)
   		session2.add(user)
   		transaction.commit()
   		session.flush()
   		if use_gpg:
		   	message=(u"Witaj "+request.params['name']+" "+request.params['surname']+"!\n"+u"Kliknij w poniższy link aby aktywować konto:\n"
		   	+request.route_url('activate_account', _query={'gpg-token':URLSafeSerializer(secret, salt='activate-salt-gpg').dumps(request.params['email'])})+"\n\n"
		   	+u"Pozdrawiamy,\nstaszic.edu.pl")
		   	send_mail(request,u"Rejestracja - staszic.edu.pl",[request.params['email']],message,fingerprint)
   		else:
		   	message=(u"Witaj "+request.params['name']+" "+request.params['surname']+"!\n"+u"Kliknij w poniższy link aby aktywować konto:\n"
		   	+request.route_url('activate_account', _query={'token':URLSafeSerializer(secret, salt='activate-salt').dumps(request.params['email'])})+"\n\n"
		   	+u"Pozdrawiamy,\nstaszic.edu.pl")
		   	send_mail(request,u"Rejestracja - staszic.edu.pl",[request.params['email']],message)
	   	return Response("Captcha correct", content_type='text/plain', status_int=500)
   return page

@view_config(route_name='forgot_password', renderer='login.mak')
def forgot_password(request):
   page={'editor':0, 'allerts':[], 'recaptcha_public':recaptcha_public, 'active':'forgot_password'}
   page.update({'css_url':request.webassets_env['r_css'].urls()[0],'js_url':request.webassets_env['r_js'].urls()[0],'libs_url':request.webassets_env['libs_js'].urls()[0]}) 
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   page['name']=username(logged_in)
   if logged_in: return HTTPFound(location = request.route_url('home'))
   if 'email' in request.params:
	   	mailer = request.registry['mailer']  
	   	message = Message(subject=u"Przypomnienie hasła - staszic.edu.pl",
			                  sender="mailer.staszic@gmail.com",
			                  recipients=[request.params['email']],
			                  body=u"Witaj "+request.params['name']+" "+request.params['surname']+"!\n"
			                  +u"Kliknij w poniższy link aby aktywować konto:\n"
			                  +request.route_url('forgot_password', _query={'token':URLSafeSerializer(secret, salt='new_password-salt').dumps(request.params['email'])})+"\n\n"
			                  +u"Pozdrawiamy,\nstaszic.edu.pl"
			                  )
	   	mailer.send_immediately(message)
   return page
   
@view_config(route_name='activate_account', renderer='login.mak')
def activate_account(request):
   page={'editor':0, 'allerts':[], 'recaptcha_public':recaptcha_public, 'active':'forgot_password'}
   page.update({'css_url':request.webassets_env['r_css'].urls()[0],'js_url':request.webassets_env['r_js'].urls()[0],'libs_url':request.webassets_env['libs_js'].urls()[0]}) 
   logged_in = authenticated_userid(request)
   page['logged_in']=logged_in
   page['name']=username(logged_in)
   sig_okay, email = URLSafeSerializer(secret, salt='activate-salt').loads_unsafe(request.params['token'])
   if sig_okay:
   	page['allerts'].append([email,"information","topRight"])
   else:
   	page['allerts'].append([u"Token aktywacyjny wygasł.","information","topRight"])
   return page
   
   
def is_pesel_correct(pesel):
   if len(pesel)!=11 or not pesel.isnumeric():
   	return False   	
   sum, ct = 0, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
   for i in range(11):
      sum += (int(pesel[i]) * ct[i])
   return (str(sum)[-1] == '0')

def is_date_correct(date):
	try:
		datetime.datetime.strptime(date, '%d/%m/%Y').date()
		return True
	except:
		return False 