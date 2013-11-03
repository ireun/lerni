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
    page['who']=""
    page['lessons'] = [['1', [], [], [], [], []],['2', [], [], [], [], []],
                       ['3', [], [], [], [], []],['4', [], [], [], [], []],
                       ['5', [], [], [], [], []],['6', [], [], [], [], []],
                       ['7', [], [], [], [], []],['8', [], [], [], [], []]]
    page['lessons2'] = [['1', [], [], [], [], []],['2', [], [], [], [], []],
                       ['3', [], [], [], [], []],['4', [], [], [], [], []],
                       ['5', [], [], [], [], []],['6', [], [], [], [], []],
                       ['7', [], [], [], [], []],['8', [], [], [], [], []]]

    if 'teacher_last_name' in request.params:
        page['who'] = request.params['teacher_last_name']
        t = page['who']
        teacher = DBSession.query(People).filter_by(first_name=t.split(" ")[0], last_name=t.split(" ")[1])
        teacher = DBSession.query(Teachers).filter_by(user_id=teacher.first().id).first()
        for position in DBSession.query(Lessons).filter_by(teacher_id=teacher.id):
            for x in DBSession.query(LessonsGroups).filter_by(lesson_id=position.id):
                page['lessons'][position.order-1][position.day+1].append(x.group.name)
                page['lessons2'][position.order-1][position.day+1].append(x.group.name)
            for x in page['lessons2'][position.order-1][position.day+1]:
                division=DBSession.query(Groups).filter_by(name=x).first().division
                all_groups=[]
                for y in DBSession.query(Groups).filter_by(division_id=division.id):
                    all_groups.append(y.name)
                if set(all_groups) <= set(page['lessons'][position.order-1][position.day+1]):
                    for z in all_groups:
                        page['lessons'][position.order-1][position.day+1].remove(z)
                    page['lessons'][position.order-1][position.day+1].append(division.name)
            page['lessons'][position.order-1][position.day+1][-1] += "["+str(position.room)+"]"
            #    page['lessons'][position.order-1][position.day+1][0].append(x.group.name)

    if 'group_name' in request.params:
        page['who'] = request.params['group_name']
        division = DBSession.query(Divisions).filter_by(name=page['who']).first()
        g_id=0
        for group in DBSession.query(Groups).filter_by(division_id=division.id):
            for x in range(8):
                for y in range(5):
                    page['lessons'][x][y+1].append("---")

            for p in DBSession.query(LessonsGroups).filter_by(group_id=group.id):
                if p.lesson.subject.name:
                    s_name = p.lesson.subject.name
                else:
                    s_name = "unknown"
                page['lessons'][p.lesson.order-1][p.lesson.day+1][g_id] = s_name+"["+str(p.lesson.room)+"]"
            g_id += 1
        for order in range(len(page['lessons'])):
            for lesson in range(len(page['lessons'][order])):
                l=page['lessons'][order][lesson]
                if len(l)==2 and l[0]==l[1]:
                    page['lessons'][order][lesson]=[l[0]]
    return page