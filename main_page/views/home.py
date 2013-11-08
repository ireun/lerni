# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='home', renderer='main.mak')
def home(request):
    page={'editor':False, 'allerts':''}
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
    last_video=DBSession.query(VideosMain).order_by('-id').first().video
    if last_video.hosting_id == 1:
        last_video = ""
    elif last_video.hosting_id == 2: #todo: dodanie video do Main blokuje możliwość edycji
        last_video = '<iframe src="http://player.vimeo.com/video/'+last_video.link+'"  height="315" frameborder="0"\
                      webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>'


    page['rows']=[[]]
    page['rows'][0].append([u"Ostatnie video","last_video","video",last_video,"col-md-8"])
    lern_message=u'''Strona, którą oglądasz powstała dzięki <a href="https://github.com/kamilx3/lerni">Lerni</a>.<br>
                Dla ciebie (jako ucznia) oznacza to wygodę w załatwianiu wszelkich spraw związanych ze szkołą, możliwość dzielenia się efektami swojej pozaszkolnej pracy z innymi, lepszy dostęp do materiałów edukacyjnych i informacji o konkursach.<br>
                Dla nauczyciela - mniej pracy - automatyczne sprawdzanie testów, wspomaganie wypełniania dziennika, łatwy kontakt z uczniami sprawią, że znowu można skupić się na nauczaniu.<br>
                Jeśli umiesz programować możesz pomóc w rozwoju projektu albo napisać własną aplikację korzystającą z <a href="https://github.com/kamilx3/lerni">oficjalnego api</a>.'''
    page['rows'][0].append([u"Dowiedz się więcej","learn_more","",lern_message,"col-md-4"])
    page['news']=[]
    for position in DBSession.query(TweetsMain).order_by('-id').filter_by(category_id=1).limit(8):
        page['news'].append([position.tweet.user.full_name,position.tweet.date,position.tweet.text,position.tweet.link,position.tweet.link_name])
    page['successes']=[]
    for position in DBSession.query(TweetsMain).order_by('-id').filter_by(category_id=2).limit(8):
        page['successes'].append([position.tweet.user.full_name,position.tweet.date,position.tweet.text,position.tweet.link,position.tweet.link_name])

    page['banners']=[]
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link,position.alternative])
    return page













