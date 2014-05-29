# -*- coding: utf-8 -*-
from base import *


@view_config(route_name='entries', renderer='content_text.mak', permission='view')
def entries(request):
    page = {}
    page.update(get_basic_account_info(request))
    return page


@view_config(route_name='entry', renderer='content_text.mak', permission='view')  
def entry_view(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = []
    entry = DBSession.query(Entries).filter_by(id=request.matchdict['id']).first()
    #if not entry:#
    #	return notfound#
    page['lang'] = 'pl_PL'
    page['title'] = entry.folder.last_version.title
    page['subtitle'] = entry.last_version.title
    page['keywords'] = entry.last_version.tags
    page['author'] = entry.folder.user.full_name
    page['id'] = request.matchdict['id']
    page['date'] = str(entry.date).split(" ")[0]
    page['css_data'] = ""
    page['back'] = "/folder/"+str(entry.folder.id)
    page['share_url'] = request.url
    page['share_title'] = "LOOL"
    page['leaves'] = True
    page['snow'] = True
    page['edit'] = 'edit' in request.params and page['logged_in']

    words = len(entry.last_version.text.split(" "))
    page['time'] = words/200
    soup = BeautifulSoup(entry.last_version.text)
    [s.extract() for s in soup(['script', 'iframe', 'img', 'object', 'embed', 'param'])]
    page['content'] = parser.format(unicode(soup), somevar='somevalue')
    if 'pdf' in request.params:
        css = ["entries.css", "content.css"]
        for x in css:
            css_file = open("main_page/static/css/"+x)
            page['css_data'] += "\n"+css_file.read()
            css_file.close()
        return response_pdf(request, unicode(render('content_text.mak', page, request)),
                            filename=page['title']+"-"+page['subtitle'])
    return page


@view_config(route_name='user', renderer='pages.mak', permission='view')
def user_view(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    logged_in = authenticated_userid(request)
    page['logged_in'] = logged_in
    page['name'] = username(logged_in)
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
    user = DBSession.query(People).filter_by(url_name=request.matchdict['id']).first().full_name
    page['rows'] = [[["", "12", "", user]]]
    return page
#@view_config(route_name='entry_pdf', permission='view')
#def entry_pdf(request):
#	renderer_dict = {'editor':0, 'allerts':[]}
#	entry = DBSession.query(Entries).filter_by(id=request.matchdict['id']).first()
#	renderer_dict.update({'lang':'pl_PL','title':entry.folder.last_version.title,'subtitle': entry.last_version.title,
#	'keywords':entry.last_version.tags,'author':entry.folder.user.first_name+" "+entry.folder.user.last_name,
#	'id':request.matchdict['id'],'date':str(entry.date).split(" ")[0]})
#	soup = BeautifulSoup(entry.last_version.text);[s.extract() for s in soup(['script','iframe'])];
#	renderer_dict['content']=parser.format(unicode(soup), somevar='somevalue')
#	renderer_dict['css_data']=""
#	css=["entries.css","content.css"]
#	for x in css:
#		css_file=open("main_page/static/styles/"+x);renderer_dict['css_data']+="\n"+css_file.read();css_file.close()
#	return response_pdf(request, unicode(render('content_text_pdf.mak', renderer_dict, request)),
            # filename=renderer_dict['title']+"-"+renderer_dict['subtitle'])


@view_config(route_name='folder', renderer='content_text.mak', permission='view')
def folder_view(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = []
    page.update(get_basic_account_info(request))
    folder = DBSession.query(Folders).filter_by(id=request.matchdict['id']).first()
    page['lang'] = 'pl_PL'
    page['title'] = folder.last_version.title
    page['subtitle'] = u"Spis treści"
    page['keywords'] = folder.last_version.tags
    page['author'] = folder.user.full_name
    page['id'] = request.matchdict['id']
    #folder.date
    page['date'] = ""
    page['css_data'] = ""
    page['snow'] = True
    page['content'] = ""
    page['back'] = "/"
    page['share_url'] = "http://www.google.pl"
    page['share_title'] = "LOOL"

    for entry in folder.entries:
        page['content'] += '<a href="/entry/'+str(entry.id)+'">'+entry.last_version.title+'</a>'
    return page


@view_config(route_name='entry_save', renderer='jsonp')
def entries_save(request):
    l = json.loads
    #d = json.dumps

    if 'text' in request.params:
        a = l(request.params['text'])
        pairs = [(k, v) for (k, v) in a.iteritems()]
        entry_id = pairs[0][0]
        data = pairs[0][1]
        entry = DBSession.query(Entries).filter_by(id=entry_id).first().last_version
        entry.text = data
        transaction.commit()
        return{'status': True}
    return{'status': False}


@view_config(route_name='loading', renderer='loading.mak', permission='view')
def loading(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    return page


@view_config(route_name='radio', renderer='apps.mak')
##idiki originalne - lerni zapisze sobie original article id [locallink][/locallink]  [map][/map]
def about(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['boxes'] = [[u"Historia Szkoły", ""], [u"Patron", ""], [u"Honorowy Patron", ""],
                    [u"Absolwenci", ""], [u"Fundacja", ""], [u"Towarzystwo Szkół Twórczych", ""],
                    [u"Statut Szkoły", ""], [u"Szkolne Muzeum", ""], [u"Regulamin Szkoły", ""], [u"Galeria", ""],
                    [u"Kontakt", ""], [u"Dojazd", "/p/dojazd"], [u"Plan lekcji", ""], [u"Panorama", ""],
                    [u"Kalendarium", ""], [u"Staszic na Facebooku", ""]]
    return page