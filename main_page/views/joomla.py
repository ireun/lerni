# -*- coding: utf-8 -*-
from base import *
import psutil
from pyramid.security import authenticated_userid
import datetime

from sqlalchemy import create_engine


@view_config(route_name='joomla', renderer='joomla.mak')
def admin_log_graduates(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Absolwenci"]], 'allerts': []}
    page['articles'] = []
    page['page_title'] = "ZSO nr 15 w Sosnowcu"
    page['page_id'] = 1
    if 'page' in request.params:
        try:
            page['page_id'] = int(request.params['page'])
        except:
            pass
    page['banners'] = []
    for position in DBSession.query(Banners).limit(6):
        page['banners'].append([position.link, position.alternative])

    page['tweets'] = []
    c = DBSession.query(TweetsCategoriesList).filter_by(name="successes").first()
    for position in DBSession.query(TweetsCategories).order_by('-id').filter_by(category=c).limit(8):
        page['tweets'].append({'full_name': position.tweet.user.full_name,
                               'time': position.tweet.date,
                               'text': position.tweet.text,
                               'link': position.tweet.link,
                               'link_name': position.tweet.link_name})

    lucky_number = DBSession.query(LuckyNumbers).filter_by(date=datetime.datetime.now().date() + datetime.timedelta(1))
    lucky_number = lucky_number.first()
    try:
        page['lucky_number'] = lucky_number.number
        page['lucky_number_date'] = lucky_number.date
    except AttributeError:
        page['lucky_number'] = "??"
        page['lucky_number_date'] = ""
    week = get_week(datetime.datetime.now().date() + datetime.timedelta(1))
    page['numbers'] = []
    for x in DBSession.query(LuckyNumbers).filter(LuckyNumbers.date.between(week[0], week[1])):
        page['numbers'].append([x.date, x.number])
    all_numbers = range(37)
    all_numbers.remove(0)
    for x in DBSession.query(LuckyNumbers).order_by(asc(LuckyNumbers.date)):
        if x.number in all_numbers:
            all_numbers.remove(x.number)
        else:
            all_numbers = range(37)
            all_numbers.remove(0)
    page['left'] = sorted(all_numbers)

    engine = create_engine('mysql://kamil:tajne_haslo@192.168.0.3/staszic?charset=utf8')
    #engine.raw_connection().connection.text_factory = unicode
    connection = engine.connect()
    result = connection.execute("select * from j25_content where state=1 order by created desc limit " +
                                str((page['page_id'] - 1) * 10) + "," + str((page['page_id']) * 10))
    for row in result:
        page['articles'].append({'title': row['title'],
                                 'introtext': row['introtext'],
                                 'fulltext': row['fulltext'].strip() != "",
                                 'time': row['created'],
                                 'created': row['created'].strftime("%a, %d %B %Y"),
                                 'id': row['id'],
                                 'alias': row['alias']
        })
    connection.close()
    return page