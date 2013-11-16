# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='sis_home', renderer='sis/home.mak')
def sis_home(request):
    page={'editor':0, 'allerts':[]}
    page['last_update'] = '2013-11-01'
    return page
@view_config(route_name='sis_about', renderer='sis/about.mak')
def sis_about(request):
    page={'editor':0, 'allerts':[]}
    page['last_update'] = '2013-11-01'
    return page
@view_config(route_name='schedule', renderer='sis/timetable.mak')
def plan(request):
    page={'editor':0, 'allerts':[]}
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
    page = dict(editor=0, allerts=[])
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