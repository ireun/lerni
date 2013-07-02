# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='zastepstwa', renderer='zastepstwa.mak')   #, permission='edit'
def my_view2(request):
    breadcrumbs=[["/zastepstwa",u"Zastępstwa"]]
    try:
       menu_top_list =[]
       for position in DBSession.query(MenuTop):
       	menu_top_list.append([position.link,position.name])       
       if has_permission('view_subs', request.context, request): ### Tak jest źle !! dodać not i może coś jeszcze
       	return {'menu_top_list':menu_top_list , 'knows_password':False}
       logged_in = authenticated_userid(request)
       if logged_in:
       	name=DBSession.query(People).filter_by(login=logged_in).first().username
       locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')
       substitutions_query=DBSession.query(Substitutions).order_by(desc(Substitutions.id)).first()
       date_for = substitutions_query.date_for
       date_for2 = substitutions_query.date_for
       substitutions_id=substitutions_query.id
       months=[u"stycznia",u"lutego",u"marca",u"kwietnia",u"maja",u"czerwca",u"lipca",u"sierpnia",u"września",u"października",u"listopada",u"grudnia"]
       month=months[date_for.month-1]
       date_for = str(date_for.day)+" "+month+" "+date_for.strftime("%Y r. (%A)").decode('utf-8')
       absent_list=[]
       for position in DBSession.query(Absent).filter(Absent.substitutions_id == substitutions_id):
       	teacher=DBSession.query(People).filter(People.id==position.teacher_id).first()
       	teacher_full=teacher.first_name + " " + teacher.last_name
       	lesson=lessons_get(position.teacher_id,date_for2.weekday())
       	if not position.lesson1: lesson[0]=""
       	if not position.lesson2: lesson[1]=""
       	if not position.lesson3: lesson[2]=""
       	if not position.lesson4: lesson[3]=""
       	if not position.lesson5: lesson[4]=""
       	if not position.lesson6: lesson[5]=""
       	if not position.lesson7: lesson[6]=""
       	if not position.lesson8: lesson[7]=""
       	absent_list.append([teacher_full,position.reason,lesson])
       replace_list=[]
       for position in DBSession.query(Replace).filter(Replace.substitutions_id == substitutions_id):
       	teacher=DBSession.query(People).filter(People.id==position.teacher_id).first()
       	teacher_full=teacher.first_name + " " + teacher.last_name
       	lesson=lessons_get(position.teacher_id,date_for2.weekday())
       	lesson2=[position.c1_id, position.c1_g1, position.c1_g2, position.c2_id, position.c2_g1, position.c2_g2,
       	position.c3_id, position.c3_g1, position.c3_g2, position.c4_id, position.c4_g1, position.c4_g2,
       	position.c5_id, position.c5_g1, position.c5_g2, position.c6_id, position.c6_g1, position.c6_g2,
       	position.c7_id, position.c7_g1, position.c7_g2, position.c8_id, position.c8_g1, position.c8_g2]
       	lesson3=[]
       	za_klase=[]
       	for w in range(8):
       		y=groupname_get(lesson2[w*3-2],lesson2[w*3-1],lesson2[w*3])
       		lesson3.append(y)
       		if lesson2[w]!="[]" and lesson[w]!="":
       			za_klase.append(lesson[w])       				
       	replace_list.append([teacher_full,",".join(za_klase),lesson3])
       duty_list=[]
       for position in DBSession.query(Duty).filter(Duty.substitutions_id == substitutions_id):
       	teacher=DBSession.query(People).filter(People.id==position.teacher1_id).first()
       	teacher1_full=teacher.first_name + " " + teacher.last_name
       	shift = DBSession.query(Shift).filter(Shift.id==position.shift_id).first().name
       	place = DBSession.query(Places).filter(Places.id==position.place_id).first().name
       	teacher=DBSession.query(People).filter(People.id==position.teacher2_id).first()
       	teacher2_full=teacher.first_name + " " + teacher.last_name
       	duty_list.append([teacher1_full,shift+u" - "+place,teacher2_full])
       	
    except DBAPIError:
        return Response("SQL ERROR", content_type='text/plain', status_int=500)
    return {'menu_top_list':menu_top_list , 'date_for':date_for, 'absent_list':absent_list, 'replace_list':replace_list, "duty_list":duty_list, 'knows_password':True,
     'logged_in':logged_in, 'name':name, 'breadcrumbs':breadcrumbs}
     
     
def lessons_get(t_id,day):
    to_return=[]
    for x in [1,2,3,4,5,6,7,8]:
    	for y in DBSession.query(TeacherSubject).filter(TeacherSubject.teacher_id==t_id):
    		lesson1_query = DBSession.query(Lessons).filter(Lessons.teacher_subject_id==y.id).filter(Lessons.day==day).filter(Lessons.order==x)
    		if not lesson1_query.first() is None:
    			temp2=[]
    			for position in lesson1_query:
    				group_id = position.group_id
    				temp2.append(groupname_get(group_id,position.part_1,position.part_2))
    			to_return.append("/".join(temp2))
    		else:
    			to_return.append("")
    return to_return

def groupname_get(group_id,part_1,part_2):
    temp=""
    groups_guery = DBSession.query(Groups).filter(Groups.id==group_id).first()
    year = str(8-groups_guery.year_id)
    temp = temp + year+groups_guery.name
    if part_1 and part_2:
    	pass
    elif part_1:
    	temp+="1"
    elif part_2:
    	temp+="2"
    else:
    	temp=""
    return temp
    
def groupname_get2(group_id):
    to_return=[]
    group_id=eval(group_id)
    for x in group_id:
    	x=str(x)
    	if x.find(".")!=-1:
    		part_1=False
    		part_2=False  	
    		if x[x.find(".")+1:]=="1" : part_1 = True
    		elif x[x.find(".")+1:]=="2": part_2 = True
    		else: part_1 = 1; part_2 = 1
    		x=x[:x.find(".")]
    	else: part_1=True; part_2=True
    	temp=""
    	groups_guery = DBSession.query(Groups).filter(Groups.id==x).first()
    	year = str(8-groups_guery.year_id)
    	temp = temp + year+groups_guery.name
    	if part_1 and part_2:
    		pass
    	elif part_1:
    		temp+="1"
    	elif part_2:
    		temp+="2"
    	else:
    		temp=""
    	to_return.append(temp)
    return "/".join(to_return)