# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='support', renderer='pages.mak')
def support(request):
    page={'editor':0, 'allerts':[]}
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['name']=username(logged_in)
    page['menu_top_list']=menu_top(request)
    page['banners']=[]
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link,position.alternative])
    page['rows']=[[],[],[],[],[],[],[],[],[],[]]
    for position in DBSession.query(Pages).filter_by(url_name="support").first().widgets:
        page['rows'][position.row].append(["",position.size_x,position.data])
    return page
   
@view_config(route_name='support_ask', renderer='support_ask.mak')
def support_ask(request):
    page = {'editor':0, 'allerts':[], 'recaptcha_public':recaptcha_public}
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    if 'topic' in request.params:
        topic = request.params['topic']
        section_select = request.params['section_select']
        question = request.params['question']
        importance = request.params['importance']
        captcha = request.params['captcha']
        sub_section_id=DBSession.query(SupportSubSections).filter_by(short_name=section_select).first().id
        time_now=datetime.datetime.now()
        if logged_in:
            page['allerts'].append([u"Wiadomość została wysłana :)","success","topRight"])
            email = DBSession.query(People).filter_by(login=logged_in).first().email
            with transaction.manager:
                DBSession.add_all([SupportTickets(sub_section_id, topic, email, "", importance, True, "", time_now)])
            last_id=DBSession.query(SupportTickets).order_by("id desc").first().id ### Zrobić to jakoś normalnie....
            with transaction.manager:
                DBSession.add_all([SupportQuestions(last_id, question, time_now)])
        else:
            page['allerts'].append([u"Wiadomość została wysłana, sprawdź emaila w celu uwierzytelnienia.","success","topRight"])
            email = request.params['email']
            password = request.params['password']
            act_hash=hashlib.sha224(str(random.random())).hexdigest()[:10]
            with transaction.manager:
                DBSession.add_all([
                    SupportTickets(sub_section_id, topic, email, password, importance, False, act_hash, time_now)
                ])
            last_id=DBSession.query(SupportTickets).order_by("id desc").first().id
            with transaction.manager:
                DBSession.add_all([SupportQuestions(last_id, question, time_now)])
            mailer = request.registry['mailer']
            message = Message(subject=u"Dziękujemy za zadanie pytania!",
                              sender="mailer.staszic@gmail.com",
                              recipients=[email],
                              body=u"Twoje zapytanie zostało odebrane, aby potwierdzić swoją tożsamość kliknij link poniżej.\n"
                              +request.route_url('support_ask_ticket', id = last_id, _query={'auth_code':act_hash})
                              )
            mailer.send(message)
    try:
        page['menu_top_list']=[]
        for position in DBSession.query(MenuTop):
            page['menu_top_list'].append([position.link,position.name])
            page['name']=""
        if logged_in:
            page['name']=DBSession.query(People).filter_by(login=logged_in).first().username
        else:
            page['allerts'].append([u"Aby zobaczyć otwarte przez siebie tickety musisz być zalogowany!","warning","topRight"])
            page["sections"]=[]
        for position in DBSession.query(SupportSections):
            page["sections"].append([position.name,[]])
            for position2 in DBSession.query(SupportSubSections).filter_by(section_id=position.id):
                page["sections"][-1][1].append([position2.name,position2.short_name])
    except DBAPIError:
        return Response("Mysql connection error", content_type='text/plain', status_int=500)
    page['allerts'].append([u"Użyj pokrętła, aby ocenić jak szybkiej reakcji wymaga Twój problem.","allert","topRight"])
    return page
   
@view_config(route_name='support_ask_ticket', renderer='support_ask_ticket.mak')
def support_ask_ticket(request):
    try:
        ticket_num=int(request.matchdict['id'])
        DBSession.query(SupportTickets).filter_by(id=ticket_num).first().confirmed
    except:
        raise exception_response(404)
    if DBSession.query(SupportTickets).filter_by(id=ticket_num).first().confirmed:
        if 'auth_code' in request.params:
            raise exception_response(403)
        if 'email' in request.params:
            email = request.params['email']
        if not DBSession.query(SupportTickets).filter_by(id=ticket_num).first().email==email:
            raise exception_response(403)
    elif 'auth_code' in request.params:
        auth_code = request.params['auth_code']
        if auth_code == DBSession.query(SupportTickets).filter_by(id=ticket_num).first().confirmation_code:
            DBSession.query(SupportTickets).filter_by(id=ticket_num).first().confirmed=True
            user_email=DBSession.query(SupportTickets).filter_by(id=ticket_num).first().email
            mailer = request.registry['mailer']
            message = Message(subject=u"Tożsamość potwierdzona.",
                              sender="mailer.staszic@gmail.com",
                              recipients=[user_email],
                              body=u"Aby kolejnym razem wrócić do wątku użyj poniższego linku.\n"
                              +request.route_url('support_ask_ticket',id = ticket_num,_query={'email':user_email})
                              )
            mailer.send(message)
            return HTTPFound(location = request.route_url('support_ask_ticket',id = ticket_num,_query={'email':user_email}))
        else:
            raise exception_response(403)
    else:
        raise exception_response(403)
    page={'editor':0, 'breadcrumbs':[["","Support"],["","Ticket-"+str(ticket_num)]], 'menu_left_list':menu_left_list, 'allerts':[]}
    page['ticket_num']=ticket_num
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    return page









