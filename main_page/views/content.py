# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='entries', renderer='content_text.mak', permission='view')
def entries(request):
    return {}

@view_config(route_name='entry', renderer='content_text.mak', permission='view')  
def entry(request):
    page = {'editor':0, 'allerts': []} #referrer #
    page['page_title']="ZSO nr 15 w Sosnowcu"
    page['banners']=[]
    logged_in = authenticated_userid(request)
    try: user = DBSession.query(People).filter_by(email=logged_in).first()
    except DBAPIError: return Response("Mysql connection error", content_type='text/plain', status_int=500)
    entry = DBSession.query(Entries).filter_by(id=request.matchdict['id']).first()
    #if not entry:#
    #	return notfound#
    page['lang']='pl_PL'
    page['title']=entry.folder.last_version.title  #'flattr_uid':entry.folder.user.flattr_uid,'flattr_category':entry.last_version.flattr_category#
    page['subtitle']=entry.last_version.title      #'lerni_link':entry.lerni_link})#
    page['keywords']=entry.last_version.tags
    page['author']=entry.folder.user.full_name
    page['id']=request.matchdict['id']
    page['date']=str(entry.date).split(" ")[0]
    page['css_data']=""
    page['back'] = "/folder/"+str(entry.folder.id)
    page['share_url']=request.url
    page['share_title']="LOOL"
    page['leaves']=True
    page['snow']=True

    words = len(entry.last_version.text.split(" "))
    page['time'] = words/200
    soup = BeautifulSoup(entry.last_version.text)
    [s.extract() for s in soup(['script','iframe','img','object','embed','param'])];
    page['content'] = parser.format(unicode(soup), somevar='somevalue')
    if 'pdf' in request.params:
        css=["entries.css","content.css"]
        for x in css:
            css_file=open("main_page/static/css/"+x);page['css_data']+="\n"+css_file.read();css_file.close()
        return response_pdf(request, unicode(render('content_text.mak', page, request)), filename=page['title']+"-"+page['subtitle'])
    return page

@view_config(route_name='user', renderer='pages.mak', permission='view')
def user(request):
    page={'editor':0, 'allerts':[]}
    page['page_title']="ZSO nr 15 w Sosnowcu"
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['name']=username(logged_in)
    page['banners']=[]
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link,position.alternative])
    page_user = DBSession.query(People).filter_by(url_name=request.matchdict['id']).first().full_name
    page['rows']=[[["","12","", page_user]]]
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
#	return response_pdf(request, unicode(render('content_text_pdf.mak', renderer_dict, request)), filename=renderer_dict['title']+"-"+renderer_dict['subtitle'])

@view_config(route_name='folder', renderer='content_text.mak', permission='view')
def folder(request):
   page={'editor':0, 'allerts':[]}
   page['page_title']="ZSO nr 15 w Sosnowcu"
   page['banners']=[]
   logged_in = authenticated_userid(request)
   try: user = DBSession.query(People).filter_by(email=logged_in).first()
   except DBAPIError: return Response("Mysql connection error", content_type='text/plain', status_int=500)   
   folder = DBSession.query(Folders).filter_by(id=request.matchdict['id']).first()
   page['lang']='pl_PL'
   page['title']=folder.last_version.title
   page['subtitle']=u"Spis treści"
   page['keywords']=folder.last_version.tags
   page['author']=folder.user.full_name
   page['id']=request.matchdict['id']
   page['date']=""#folder.date
   page['css_data']=""
   page['snow']=True
   page['content'] = ""
   page['back'] = "/"
   page['share_url']="http://www.google.pl"
   page['share_title']="LOOL"

   for entry in folder.entries:
    page['content']+='<a href="/entry/'+str(entry.id)+'">'+entry.last_version.title+'</a>'
   return page


@view_config(route_name='entry_save', renderer='jsonp')
def entries_save(request):
    try: user = DBSession.query(People).filter_by(email=logged_in).first()
    except DBAPIError: return Response("Mysql connection error", content_type='text/plain', status_int=500)
    if 'raptor-content' in request.params:
        pairs = [(k, v) for (k, v) in json.loads(request.params['raptor-content']).iteritems()]
        entry_id=pairs[0][0]
        data=pairs[0][1]
        #request.params['postName']
        #request.params['id']
        #request.params['email']
        return{'status':True}
    return{'status':False}

@view_config(route_name='loading', renderer='loading.mak', permission='view')
def loading(request):
   page={'editor':0, 'allerts':[]}
   logged_in = authenticated_userid(request)
   try:
    user = DBSession.query(People).filter_by(email=logged_in).first()
   except DBAPIError:
      return Response("Mysql connection error", content_type='text/plain', status_int=500)
   return page

@view_config(route_name='radio', renderer='apps.mak') ##idiki originalne - lerni zapisze sobie original article id [locallink][/locallink]  [map][/map]
def about(request):
    page={'editor':0, 'allerts':[]}
    page['boxes']=[[u"Historia Szkoły",""],[u"Patron",""],[u"Honorowy Patron",""],
    [u"Absolwenci",""],[u"Fundacja",""],[u"Towarzystwo Szkół Twórczych",""],[u"Statut Szkoły",""],
    [u"Szkolne Muzeum",""],[u"Regulamin Szkoły",""],[u"Galeria",""],[u"Kontakt",""],
    [u"Dojazd","/p/dojazd"],[u"Plan lekcji",""],[u"Panorama",""],[u"Kalendarium",""],[u"Staszic na Facebooku",""]]
    return page