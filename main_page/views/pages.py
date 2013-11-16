# -*- coding: utf-8 -*-
from base import *
from pyramid.request import Request
import pyramid
@view_config(route_name='page', renderer='pages.mak')
def successes(request):
    page={'editor':0, 'allerts':[]}
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['name']=username(logged_in)
    page['menu_top_list']=menu_top(request)
    page['banners']=[]
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link,position.alternative])
    page['rows']=[[],[],[],[],[],[],[],[],[],[]]
    for position in DBSession.query(Pages).filter_by(url_name=request.matchdict['id']).first().widgets:
        soup = BeautifulSoup(position.data)
        [s.extract() for s in soup(['script','iframe','img','object','embed','param'])];
        data = parser.format(unicode(soup), somevar='somevalue')
        page['rows'][position.row].append(["",position.size_x,data])
    return page

@view_config(route_name='set', renderer='grid.mak') ##idiki originalne - lerni zapisze sobie original article id [locallink][/locallink]  [map][/map]
def set(request):
    page={'editor':0, 'allerts':[]}
    page['boxes']=[]
    for position in DBSession.query(Sets).filter_by(id=request.matchdict['id']).first().items:
        page['boxes'].append([position.name,position.link])
    page['banners']=[]
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link,position.alternative])
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['name']=username(logged_in)
    return page

@view_config(route_name='easy_link') ##idiki originalne - lerni zapisze sobie original article id [locallink][/locallink]  [map][/map]
def easy_link(request):
    for x in DBSession.query(EasyLinks).filter_by(name=request.matchdict['link']):
        subreq = Request.blank(x.path)
        subreq.cookies = request.cookies #pass authentication data
        response = request.invoke_subrequest(subreq)
        return response
    return HTTPNotFound()


@view_config(route_name='connection')
def competitions(request):
    username = request.params['username'] + request.params['n1a'] + request.params['n2a'] + request.params['n3a'] + request.params['n4a'] + request.params['n1b'] + request.params['n2b'] + request.params['n3b'] + request.params['n4b'] + request.params['n1c'] + request.params['n2c'] + request.params['n3c'] + request.params['n4c'] + request.params['n1d'] + request.params['n2d'] + request.params['n3d'] + request.params['n4d'] + request.params['n1e'] + request.params['n2e'] + request.params['n3e'] + request.params['n4e'] + request.params['n1f'] + request.params['n2f'] + request.params['n3f'] + request.params['n4f']
    print(username)
    response = Response(body='10', content_type='text/plain')
    return response

@view_config(route_name='gallery', renderer='gallery.mak')
def gallery(request):
    page={'editor':0, 'allerts':[]}
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in

    page['breadcrumbs']=[["","Galeria"]]
    page['menu_left_list'] =[]
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    return page




