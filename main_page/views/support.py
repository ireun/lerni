# -*- coding: utf-8 -*-
from base import *


@view_config(route_name='support_ask', renderer='message.mak',
             request_param=['action', 'topic', 'email'])
def support_ticket_send(request):
    page = {'editor': 0, 'allerts': [], 'recaptcha_public': recaptcha_public}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
    logged_in = authenticated_userid(request)
    page['logged_in'] = logged_in
    page['name'] = username(logged_in)
    r = request.params

    sub_section_id = DBSession.query(SupportSubSections).filter_by(short_name=r['section_select']).first().id
    time_now = datetime.datetime.now()
    session = DBSession()
    if not 'sex' in request.params:
        sex = None
    elif r['sex'] == "male":
        sex = 1
    else:
        sex = 0
    ticket = SupportTickets(sub_section_id, r['topic'], r['email'], r['phone_number'], sex, 50, False, None, time_now)
    session.add(ticket)
    session.flush()
    ticket_id = ticket.id
    confirmation_code = URLSafeSerializer(secret, salt='support_ticket').dumps([r['email'], ticket_id])
    ticket.confirmation_code = confirmation_code
    transaction.commit()

    with transaction.manager:
        DBSession.add_all([SupportQuestions(ticket_id, r['question'], time_now, r['name'])])
    mailer = request.registry['mailer']
    message = Message(subject=u"Dziękujemy za zadanie pytania!",
                      sender="mailer.staszic@gmail.com",
                      recipients=[r['email']],
                      body=u"Twoje zapytanie zostało odebrane, aby potwierdzić swoją tożsamość kliknij link poniżej.\n"
                      + request.route_url('support_ask_ticket', id=confirmation_code)
                      )
    mailer.send(message)
    #[u"Wiadomość została wysłana, sprawdź emaila w celu uwierzytelnienia.","success","topRight"]
    return page


@view_config(route_name='support_ask', renderer='support_ask.mak')
def support_ask(request):
    page = {'recaptcha_public': recaptcha_public}
    page.update(get_basic_account_info(request))
    page['banners'] = []
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
    page['sections'] = []
    for position in DBSession.query(SupportSections):
        page["sections"].append([position.name, []])
        for position2 in DBSession.query(SupportSubSections).filter_by(section_id=position.id):
            page["sections"][-1][1].append([position2.name, position2.short_name])
    return page


@view_config(route_name='support_ask_ticket', renderer='support_ask_ticket.mak', request_param=['answer'])
def support_ask_ticket_anser(request):
    time_now = datetime.datetime.now()
    r = request.params
    ticket = DBSession.query(SupportTickets).filter_by(confirmation_code=request.matchdict['id']).first()
    if not ticket:
        raise exception_response(404)
    name = DBSession.query(SupportQuestions).filter_by(ticket=ticket).first().name
    DBSession.add_all([SupportQuestions(ticket.id, r['answer'], time_now, name)])
    return HTTPFound("")


@view_config(route_name='support_ask_ticket', renderer='support_ask_ticket.mak')
def support_ask_ticket(request):
    page = {'editor': 0, 'allerts': [], 'recaptcha_public': recaptcha_public}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
    logged_in = authenticated_userid(request)
    page['logged_in'] = logged_in
    page['name'] = username(logged_in)
    ticket = DBSession.query(SupportTickets).filter_by(confirmation_code=request.matchdict['id']).first()
    if not ticket:
        raise exception_response(404)
    page['ticket_id'] = ticket.topic
    page['messages'] = []
    for x in DBSession.query(SupportQuestions).filter_by(ticket=ticket).order_by(SupportQuestions.add_date):
        page['messages'].append(["kamilx3@gmail.com", x.add_date, x.text])
    return page

#if logged_in:
#    page['allerts'].append([u"Wiadomość została wysłana :)","success","topRight"])
#    email = DBSession.query(People).filter_by(login=logged_in).first().email
#    with transaction.manager:
#        DBSession.add_all([SupportTickets(sub_section_id, topic, email, "", importance, True, "", time_now)])
#    last_id=DBSession.query(SupportTickets).order_by("id desc").first().id ### Zrobić to jakoś normalnie....
#    with transaction.manager:
#        DBSession.add_all([SupportQuestions(last_id, question, time_now)])