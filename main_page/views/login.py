# -*- coding: utf-8 -*-
from base import *


@view_config(route_name='login', renderer='login.mak')
## Dodać "Aby zobaczyć tą stronę musisz się zalogować"###
def login_view(request):
    page = {'editor': 0, 'allerts': [], 'recaptcha_public': recaptcha_public}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['active'] = {'forgot_password': '', 'register': '', 'login': 'active'}
    next_page = request.referer or request.url
    if next_page == request.route_url('login'):
        next_page = request.route_url('home')
    if page['logged_in']:
        return HTTPFound(location=next_page)
    if {'login', 'password'} <= set(request.params):
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        session = DBSession()
        user = DBSession.query(People).filter_by(email=login).first()
        if user and user.check_password(password):
            if 'remember_me' in request.params:
                headers = remember(request, login, max_age=60*60*24*7)
            else:
                headers = remember(request, login)
            user.last_login = datetime.datetime.now()
            session.add(AALogin(user.id, request.client_addr, request.user_agent, str(request.accept_language),
                                datetime.datetime.now()))
            transaction.commit()
            return HTTPFound(location=next_page, headers=headers)
        page['allerts'].append([u"Zła nazwa użytkownika bądź hasło", "information", "topRight"])
    return page


@view_config(route_name='logout')
def logout(request):
    next_page = request.params.get('next') or request.route_url('home')
    headers = forget(request)
    return HTTPFound(location=next_page, headers=headers)