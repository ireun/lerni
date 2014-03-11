# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='home', renderer='pages.mak')
def home(request):
    page={'editor':False, 'allerts':''}
    page['page_title']="ZSO nr 15 w Sosnowcu"
    page['css_url']=""
    breadcrumbs=[]
    editor=0
    page_num=1
    page['name']=""
    if has_permission('edit_articles', request.context, request):
        editor=1
    page['logged_in'] = authenticated_userid(request)
    try:
        name=""
        if page['logged_in']:
            page['name']=username(page['logged_in'])
    except DBAPIError:
        return Response("SQL ERROR", content_type='text/plain', status_int=500)

    page['rows']=[[],[],[],[],[],[],[],[],[],[]]
    for position in DBSession.query(Pages).filter_by(url_name="main_page").first().widgets:
        soup = BeautifulSoup(position.data)
        [s.extract() for s in soup(['script','iframe','img','object','embed','param'])];
        data = parser.format(unicode(soup), somevar='somevalue')
        page['rows'][position.row].append(["", position.size_x, position.add_class, data])

    page['banners']=[]
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link,position.alternative])
    return page













