# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='schedule', renderer='sis/timetable.mak')
def plan(request):
    page={'editor':0, 'allerts':[]}
    page['last_update'] = '2013-11-01'
    page['groups'] = []
    page['teachers'] = []
    for position in DBSession.query(Teachers):
        if DBSession.query(Lessons).filter_by(teacher_id=position.id).first():
            page['teachers'].append(position.user.full_name)
    for position in DBSession.query(Groups):
        page['groups'].append(position.name)
    #    pass
    return page

@view_config(route_name='schedule', renderer='sis/timetable_show.mak', request_method='POST')
def plan_post(request):
    page = dict(editor=0, allerts=[])
    page['last_update'] = '2013-11-01'
    page['groups'] = []
    page['teachers'] = []
    page['who']=""
    page['lessons'] = [[1, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [2, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [3, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [4, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [5, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [6, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [7, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]],
                       [8, [[], ""], [[], ""], [[], ""], [[], ""], [[], ""]]]

    if 'teacher_last_name' in request.params:
        page['who'] = request.params['teacher_last_name']
        t = page['who']
        teacher = DBSession.query(People).filter_by(first_name=t.split(" ")[0], last_name=t.split(" ")[1]).first()
        for position in DBSession.query(Lessons).filter_by(teacher_id=teacher.id):
            page['lessons'][position.order-1][position.day+1][1] = position.room
            for x in DBSession.query(LessonsGroups).filter_by(lesson_id=position.id):
                page['lessons'][position.order-1][position.day+1][0].append(x.group.name)

    if 'group_name' in request.params:
        page['who'] = request.params['group_name']
        group = DBSession.query(Groups).filter_by(name=page['who']).first()
        for position in DBSession.query(LessonsGroups).filter_by(group_id=group.id):
            page['lessons'][position.lesson.order-1][position.lesson.day+1][1] = position.lesson.room
            if position.lesson.subject.name:
                page['lessons'][position.lesson.order-1][position.lesson.day+1][0].append(position.lesson.subject.name)
    return page