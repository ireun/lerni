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
        page['boxes'].append([position.name, position.link, position.thumb])
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])
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


@view_config(route_name='gallery_list', renderer='grid.mak')
def gallery_list(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = get_banners()
    l = json.loads
    d = json.dumps
    try:
        page['boxes'] = l(cache_load('gallery_boxes'))
    except AttributeError:
        page['boxes'] = []
        api_key = setting_load('flickr_api_key')
        flickr = flickrapi.FlickrAPI("02c13d4fd80e20dd799292c981eefde1", '20be53f80cb73467', )
        photosets = l(flickr.photosets_getList(user_id='98176379@N02', format='json', nojsoncallback=1, per_page=10))
        print photosets
        for photoset in photosets['photosets']['photoset']:
            images = l(flickr.photos_getSizes(photo_id=photoset['primary'], format='json', nojsoncallback=1))
            for image in images['sizes']['size']:
                if image['label'] == 'Medium 640':
                    page['boxes'].append([photoset['title']['_content'], "/gallery/"+photoset['id'], image['source']])
        cache_save('gallery_boxes', d(page['boxes']))

    #page['boxes'].append([position.name, position.link, position.thumb])
    return page


@view_config(route_name='gallery', renderer='gallery.mak')
def gallery(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['breadcrumbs'] = [["", "Galeria"]]
    gallery_id = request.matchdict['id']
    l = json.loads
    d = json.dumps
    try:
        page['images'] = l(cache_load('gallery_'+gallery_id))
    except AttributeError:
        page['images'] = []
        api_key = setting_load('flickr_api_key')
        flickr = flickrapi.FlickrAPI("02c13d4fd80e20dd799292c981eefde1", '20be53f80cb73467', )
        photos = l(flickr.photosets_getPhotos(photoset_id=gallery_id, format='json', nojsoncallback=1))
        for photo in photos['photoset']['photo']:
            new_image = {}
            images = l(flickr.photos_getSizes(photo_id=photo['id'], format='json', nojsoncallback=1))
            for image in images['sizes']['size']:
                if image['label'] == 'Original':
                    new_image['Original'] = image['source']
                if image['label'] == "Square":
                    new_image['Square'] = image['source']
            page['images'].append(new_image)
        cache_save('gallery_'+gallery_id, d(page['images']))
    return page


@view_config(route_name='syllabus', renderer='syllabus.mak')
def syllabus(request):
    year = "2014-2015"
    next_page = request.route_url('syllabus_year', year=year)
    return HTTPFound(location=next_page)


@view_config(route_name='syllabus_year', renderer='syllabus.mak')
def syllabus_year(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    year = request.matchdict['year']
    page['profiles'] = []
    try:
        for position in DBSession.query(SyllabusYears).filter_by(path_name=year).first().profiles:
            page['profiles'].append({'name': position.name, 'description': position.description,
                                     'path': request.route_url('syllabus_profile', year=year,
                                                               profile=position.path_name)})
    except:
        page['message'] = u'Podany rok nie istnieje w bazie danych'
    page['back'] = request.route_url('home')
    return page


@view_config(route_name='syllabus_profile', renderer='syllabus.mak')
def syllabus_profile(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = get_banners()
    year = request.matchdict['year']
    profile = request.matchdict['profile']
    profiles = DBSession.query(SyllabusYears).filter_by(path_name=year).first().profiles
    page['profiles'] = []
    for position in profiles.filter_by(path_name=profile).first().extensions:
        page['profiles'].append({'name': position.name, 'description': position.description,
                                 'path': request.route_url('syllabus_extension', year=year, profile=profile,
                                                           extension=position.path_name)})
    page['back'] = request.route_url('syllabus_year', year=year)
    return page

@view_config(route_name='syllabus_extension', renderer='syllabus_table.mak')
def syllabus_ext(request):
    page = {'editor': 0, 'allerts': []}
    page.update(get_basic_account_info(request))
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['banners'] = get_banners()
    year = request.matchdict['year']
    profile = request.matchdict['profile']
    page['back'] = request.route_url('syllabus_profile', year=year, profile=profile)
    return page