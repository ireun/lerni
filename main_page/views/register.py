# -*- coding: utf-8 -*-
from base import *


@view_config(route_name='register', renderer='login.mak', request_method='POST')
def register_post_all(request):
    page = {}
    response = captcha.submit(request.params['recaptcha_challenge_field'], request.params['recaptcha_response_field2'],
                              recaptcha_private, request.remote_addr)
    if request.params['name'] == "" or request.params['surname'] == "":
        page['allerts'].append([u"Zapomniałeś podać swojego imienia bądź nazwiska.", "information"])
    elif not is_pesel_correct(request.params['pesel']):
        page['allerts'].append([u"Numer pesel nie jest poprawny.", "information"])
    elif not is_date_correct(request.params['birthdate']):
        page['allerts'].append([u"Podana data urodzenia jest nieprawidłowa.", "information"])
    elif request.params['password'] != request.params['repeat-password']:
        page['allerts'].append([u"Podane hasła nie są takie same.", "information"])
    elif len(request.params['password']) < 6:
        page['allerts'].append([u"Hasło zbyt krótkie."
                                u"Aby hasło było bezpiecznie musi składać się z przynajmniej sześciu znaków.",
                                "information"])
    elif not response.is_valid:
        page['allerts'].append([u"Captcha incorrect", "information", "topRight"])
    else:
        session = DBSession(expire_on_commit=False)
        wallet = Wallet(0)
        session.add(wallet)
        ##Warto zrobić jakoś ładnie
        transaction.commit()
        session2 = DBSession()
        user = People(request.params['name'], request.params['secondname'], request.params['surname'],
                      request.params['pesel'],
                      datetime.datetime.strptime(request.params['birthdate'], '%d/%m/%Y').date(),
                      request.params['phonenumber'], request.params['email'], request.params['password'],
                      "key_data", "fingerprint", wallet.id, 0, 0, 0, 0)
        session2.add(user)
        transaction.commit()
        session.flush()
        message = (u"Witaj " + request.params['name'] + " " + request.params['surname'] + "!\n"
                   + u"Kliknij w poniższy link aby aktywować konto:\n"
                   + request.route_url('activate_account',
                                       _query={'token': URLSafeSerializer(secret, salt='activate-salt').
                                       dumps(request.params['email'])})
                   + "\n\n" + u"Pozdrawiamy,\nstaszic.edu.pl")
        send_mail(request, u"Rejestracja - staszic.edu.pl", [request.params['email']], message)
        return Response("Captcha correct", content_type='text/plain', status_int=500)
    return Response("Somethin went wrong.", content_type='text/plain', status_int=500)


@view_config(route_name='register', renderer='login.mak', request_method='POST',
             request_param=['format=jsonp', 'method=lerni.bells.types.getList', 'jtStartIndex', 'jtPageSize'])
def register_post_missing(request):
    page = {'allerts': [], 'recaptcha_public': recaptcha_public, 'active': 'register'}
    page.update(get_basic_account_info(request))
    return page


@view_config(route_name='register', renderer='login.mak')
def register(request):
    page = {'alerts': [], 'recaptcha_public': recaptcha_public, 'active': 'register'}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    return page


@view_config(route_name='forgot_password', renderer='reset_password.mak',  request_method='POST',
             request_param=['token', 'new_password', 'new_password_repeat'])
def set_password_view_change(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    r = request.params
    try:
        signed_string = URLSafeSerializer(secret, salt='new_password-salt').loads(r['token'])
        s = TimestampSigner('secret-key')
        email = s.unsign(signed_string, max_age=900)
        if r['new_password'] == r['new_password_repeat']:
            user = DBSession.query(People).filter_by(email=email).first()
            user.set_password(r['new_password'])
            user.password_date = datetime.datetime.now()
            page['alerts'].append([u"Hasło poprawnie zmieniono.", 'information'])
        else:
            page['alerts'].append([u"Hasła nie są takie same.", 'information'])
    except SignatureExpired:
        page['alerts'].append([u"Token resetu hasła wygasł.", 'information'])
    except BadSignature:
        page['alerts'].append([u"Błędna sygnatura.", 'information'])
    except BadData:
        page['alerts'].append([u"Sygnatura podpisuje inne dane.", 'information'])
    page['token'] = r['token']
    return page


@view_config(route_name='forgot_password', renderer='reset_password.mak', request_param=['token'])
def set_password_view(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    r = request.params
    try:
        signed_string = URLSafeSerializer(secret, salt='new_password-salt').loads(r['token'])
        s = TimestampSigner('secret-key')
        s.unsign(signed_string, max_age=900)
    except SignatureExpired:
        page['alerts'].append([u"Token resetu hasła wygasł.", 'information'])
    except BadSignature:
        page['alerts'].append([u"Błędna sygnatura.", 'information'])
    except BadData:
        page['alerts'].append([u"Sygnatura podpisuje inne dane.", 'information'])
    page['token'] = r['token']
    return page


@view_config(route_name='forgot_password', renderer='login.mak')
def forgot_password(request):
    page = {'allerts': [], 'recaptcha_public': recaptcha_public}
    page.update(get_basic_account_info(request))
    page['active'] = {'forgot_password': 'active', 'register': '', 'login': ''}
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['copy_right'] = "ZSO nr 15, Sosnowiec 2008-2014"
    r = request.params
    if 'email' in request.params:
        if not DBSession.query(People).filter_by(email=r['email']).first():
            page['allerts'].append([u"Nie znaleziono konta", "error"])
            return page
        renderer_dict = page
        renderer_dict['email_name'] = DBSession.query(People).filter_by(email=r['email']).first().full_name
        renderer_dict['signature'] = u"Dziękujemy,<br/>Zespół staszic.edu.pl"
        renderer_dict['email_subject'] = u"Przypomnienie hasła - staszic.edu.pl"
        renderer_dict['email_logo'] = ['http://staszic.edu.pl/static/images/h1.gif', u'Staszic Mail']
        renderer_dict['facebook'] = ['http://staszic.edu.pl/static/images/fb.gif', u'sustaszic']
        s = TimestampSigner('secret-key')
        signed_string = s.sign(request.params['email'])
        renderer_dict['recorvery_link'] = request.route_url('forgot_password',
                                                            _query={'token': URLSafeSerializer(secret,
                                                                                               salt='new_password-salt')
                                                            .dumps(signed_string)})
        mailer = request.registry['mailer']
        message = Message(subject=renderer_dict['email_subject'],
                          sender="mailer.staszic@gmail.com",
                          recipients=[request.params['email']],
                          html=unicode(render('email/password_recorvery.mak', renderer_dict, request))
                          )
        #photo_data = open("main_page/templates/email/fb.gif", "rb").read()
        #attachment = Attachment("images/fb.gif", "image/jpg", photo_data)
        #message.attach(attachment)
        mailer.send_immediately(message)
    return page


@view_config(route_name='activate_account', renderer='login.mak')
def activate_account(request):
    page = {'editor': 0, 'allerts': [], 'recaptcha_public': recaptcha_public, 'active': 'forgot_password'}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    logged_in = authenticated_userid(request)
    page['logged_in'] = logged_in
    page['name'] = username(logged_in)
    sig_okay, email = URLSafeSerializer(secret, salt='activate-salt').loads_unsafe(request.params['token'])
    if sig_okay:
        page['allerts'].append([email, "information", "topRight"])
    else:
        page['allerts'].append([u"Token aktywacyjny wygasł.", "information", "topRight"])
    return page
   
   
def is_pesel_correct(pesel):
    if len(pesel) != 11 or not pesel.isnumeric():
        return False
    p_sum, ct = 0, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    for i in range(11):
        p_sum += (int(pesel[i]) * ct[i])
    return not p_sum


def is_date_correct(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y').date()
        return True
    except ValueError:
        return False