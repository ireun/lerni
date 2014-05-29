# -*- coding: utf-8 -*-
from base import *
from pyramid.request import Request


@view_config(route_name='page', renderer='pages.mak')
def successes(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
    page['rows'] = [[], [], [], [], [], [], [], [], [], []]
    for position in DBSession.query(Pages).filter_by(url_name=request.matchdict['id']).first().widgets:
        soup = BeautifulSoup(position.data)
        [s.extract() for s in soup(['script', 'iframe', 'img', 'object', 'embed', 'param'])]
        data = parser.format(unicode(soup), somevar='somevalue')
        page['rows'][position.row].append(["", position.size_x, position.add_class, data])
    return page


##idiki originalne - lerni zapisze sobie original article id [locallink][/locallink]
@view_config(route_name='set', renderer='grid.mak')
def set_view(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['boxes'] = []
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    for position in DBSession.query(Sets).filter_by(id=request.matchdict['id']).first().items:
        page['boxes'].append([position.name, position.link])
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
    logged_in = authenticated_userid(request)
    page['logged_in'] = logged_in
    page['name'] = username(logged_in)
    return page


@view_config(route_name='easy_link')
def easy_link(request):
    for x in DBSession.query(EasyLinks).filter_by(name=request.matchdict['link']):
        subreq = Request.blank(x.path)
        #### pass authentication data ####
        subreq.cookies = request.cookies
        response = request.invoke_subrequest(subreq)
        return response
    return HTTPNotFound()


@view_config(route_name='connection')
def connection(request):
    page = {}
    page.update(get_basic_account_info(request))
    response = Response(body='10', content_type='text/plain')
    return response


@view_config(route_name='gallery', renderer='gallery.mak')
def gallery(request):
    page = {'editor': 0, 'allerts': []}
    logged_in = authenticated_userid(request)
    page['logged_in'] = logged_in
    page['breadcrumbs'] = [["", "Galeria"]]
    page['menu_left_list'] = []
    page['name'] = username(logged_in)
    return page