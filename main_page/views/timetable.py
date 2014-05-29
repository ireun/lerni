# -*- coding: utf-8 -*-
from base import *


@view_config(route_name='sis_home', renderer='sis/home.mak')
def sis_home(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    page['last_update'] = '2013-11-01'
    return page


@view_config(route_name='sis_about', renderer='sis/about.mak')
def sis_about(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    page['last_update'] = '2013-11-01'
    return page


@view_config(route_name='schedule', renderer='sis/timetable.mak')
def plan(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    page['last_update'] = '2013-11-01'
    page['groups'] = []
    page['teachers'] = []
    for position in DBSession.query(Teachers):
        if DBSession.query(Lessons).filter_by(teacher_id=position.id).first():
            page['teachers'].append(position.user.full_name)
    for position in DBSession.query(Divisions):
        page['groups'].append(position.name)
    page['groups'].sort()
    page['teachers'].sort(key=lambda teacher: teacher.split(" ")[1])
    return page


@view_config(route_name='schedule', renderer='sis/timetable_show.mak', request_method='POST')
def plan_post(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    page['last_update'] = '2013-11-01'
    page['groups'] = []
    page['teachers'] = []
    if 'teacher_last_name' in request.params:
        page['schedule'] = timetable("", "", {'teacher': request.params['teacher_last_name']}, "", "")
        page['who'] = request.params['teacher_last_name']
    if 'group_name' in request.params:
        page['schedule'] = timetable("", "", {'group': request.params['group_name']}, "", "")
        page['who'] = request.params['group_name']
    return page


@view_config(route_name='lucky', renderer='sis/lucky.mak', permission='view')
def lucky(request):
    page = {'alerts': []}
    page.update(get_basic_account_info(request))
    lucky_number = DBSession.query(LuckyNumbers).filter_by(date=datetime.datetime.now().date()+datetime.timedelta(1))
    lucky_number = lucky_number.first()
    try:
        page['lucky_number'] = lucky_number.number
        page['lucky_number_date'] = lucky_number.date
    except AttributeError:
        page['lucky_number'] = "??"
        page['lucky_number_date'] = ""
    week = get_week(datetime.datetime.now().date()+datetime.timedelta(1))
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
    return page


def get_week(day):
    start = day-datetime.timedelta(day.weekday())
    end = day+datetime.timedelta(6-day.weekday())
    return [start, end]