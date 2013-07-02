# -*- coding: utf-8 -*-
from base import *
@view_config(route_name='admin')
def my_view(request):
    return HTTPFound(location = request.route_url('admin_overview'))
    
menu_left_list = [["/admin/overview","Overview", 1],["/admin/lucky-number",u"Szczęśliwy numerek",1]]#["/admin/people",u"Ludzie", 1],["/admin/substitutions",u"Zastępstwa", 1]]
menu_left_list.append(["/admin/articles",u"Artykuły",1])
menu_left_list.append(["/admin/gallery",u"Galeria",1])
    
@view_config(route_name='admin_overview', renderer='admin_overview.mak')
def my_view2(request):
    page={'editor':0, 'breadcrumbs':[["/admin",u"Panel Administratora"],["",u"Overview"]], 'allerts':[]}
    page['menu_left_list']=menu_left_list      
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    return page
    
@view_config(route_name='admin_articles', renderer='admin_articles.mak')
def admin_articles(request):
    page={'editor':0, 'breadcrumbs':[["/admin",u"Panel Administratora"],["",u"Artykuły"]], 'allerts':[]}
    page['menu_left_list']=menu_left_list      
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    page['title']=u"Lista artykułów"
    page['competitors']=[]
    return page
    
@view_config(route_name='admin_gallery', renderer='admin_gallery.mak')
def admin_gallery(request):
    page={'editor':0, 'breadcrumbs':[["/admin",u"Panel Administratora"],["",u"Overview"]], 'allerts':[]}
    page['menu_left_list']=menu_left_list      
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    return page

@view_config(route_name='admin_lucky_number', renderer='admin_lucky_number.mak')
def lucky_number(request):
    page={'editor':0, 'breadcrumbs':[["/admin",u"Panel Administratora"],["",u"Overview"]], 'allerts':[]}
    page['menu_left_list']=menu_left_list      
    logged_in = authenticated_userid(request)
    page['logged_in']=logged_in
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    return page
    
@view_config(route_name='ram_usage')
def my_view3(request):
    total_mem_str = linecache.getline('/proc/meminfo', 1)
    total_mem = int(total_mem_str[total_mem_str[:total_mem_str.rfind(" ")].rfind(" "):total_mem_str.rfind(" ")])
    free_mem_str = linecache.getline('/proc/meminfo', 2)
    free_mem = int(free_mem_str[free_mem_str[:free_mem_str.rfind(" ")].rfind(" "):free_mem_str.rfind(" ")])
    used_mem = total_mem-free_mem
    response = Response(body='No login form submited', content_type='text/plain')
    return response
    
@view_config(route_name='admin_people', renderer='admin_people.mak')
def my_view35(request):
    page={'editor':0, 'breadcrumbs':[["",u"Dla Kandydatów"],["","Wprowadzenie"]], 'allerts':[]}
    logged_in = authenticated_userid(request)
    page['menu_top_list']=menu_top(request)
    page['name']=username(logged_in)
    page['menu_left_list']=menu_left_list
    return page

@view_config(route_name='admin_substitutions', renderer='admin_substitutions.mak')
def my_view4(request):
    logged_in = authenticated_userid(request)
    locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')
    months=[u"stycznia",u"lutego",u"marca",u"kwietnia",u"maja",u"czerwca",u"lipca",u"sierpnia",u"września",u"października",u"listopada",u"grudnia"]
    
    menu_top_list =[]
    for position in DBSession.query(MenuTop):
    	menu_top_list.append([position.link,position.name])

    substitutions=[]
    for position in DBSession.query(Substitutions).order_by(desc(Substitutions.id)):
       month=months[position.date_for.month-1]
       date_for = str(position.date_for.day)+" "+month+" "+position.date_for.strftime("%Y r. (%A)").decode('utf-8')
       link_view = request.route_url('admin_substitutions_view', id = position.id)
       link_edit = request.route_url('admin_substitutions_edit', id = position.id)
       link_del = request.route_url('admin_substitutions_del', id = position.id)
       substitutions.append([position.id,date_for,link_view,link_edit,link_del])

    
    return {'menu_top_list':menu_top_list, 'menu_left_list':menu_left_list,
    'substitutions':substitutions, 'logged_in':logged_in, 'breadcrumbs':[], 'name':'lol'}
    
@view_config(route_name='admin_substitutions_view', renderer='admin_substitutions_view.mak')   #, permission='edit'
def my_view5(request):
    try:
       menu_top_list =[]
       for position in DBSession.query(MenuTop):
       	menu_top_list.append([position.link,position.name])       
       if has_permission('view_subs', request.context, request): ### Tak jest źle !! dodać not i może coś jeszcze
       	return {'menu_top_list':menu_top_list , 'knows_password':False}

       locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')
       substitutions_query=DBSession.query(Substitutions).filter_by(id=int(request.matchdict['id'])).first()
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
       	lesson2=[position.c_ids1,position.c_ids2,position.c_ids3,position.c_ids4,position.c_ids5,position.c_ids6,position.c_ids7,position.c_ids8]
       	lesson3=[]
       	za_klase=[]
       	for w in range(8):
       		y=groupname_get2(lesson2[w])
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
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'menu_top_list':menu_top_list , 'date_for':date_for, 'absent_list':absent_list, 'replace_list':replace_list, "duty_list":duty_list, 'knows_password':True}

conn_err_msg = "SQL ERROR"

@view_config(route_name='admin_substitutions_edit', renderer='admin_substitutions_edit.mak')   #, permission='edit'
def my_view6(request):
    try:
       menu_top_list =[]
       for position in DBSession.query(MenuTop):
       	menu_top_list.append([position.link,position.name])       
       if has_permission('view_subs', request.context, request): ### Tak jest źle !! dodać not i może coś jeszcze
       	return {'menu_top_list':menu_top_list , 'knows_password':False}

       locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')
       substitutions_query=DBSession.query(Substitutions).filter_by(id=int(request.matchdict['id'])).first()
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
       	lesson2=[position.c_ids1,position.c_ids2,position.c_ids3,position.c_ids4,position.c_ids5,position.c_ids6,position.c_ids7,position.c_ids8]
       	lesson3=[]
       	za_klase=[]
       	for w in range(8):
       		y=groupname_get2(lesson2[w])
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
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'menu_top_list':menu_top_list , 'menu_left_list':menu_left_list,
    'date_for':date_for, 'absent_list':absent_list, 'replace_list':replace_list, "duty_list":duty_list, 'knows_password':True}

@view_config(route_name='admin_articles_add', renderer='admin_articles_edit.mak')
def my_view8(request):
    logged_in = authenticated_userid(request)
    menu_top_list =[]
    for position in DBSession.query(MenuTop):
    	menu_top_list.append([position.link,position.name])
    
    return {'menu_top_list':menu_top_list, 'menu_left_list':menu_left_list, 'articles':[], 'logged_in':logged_in}


######################################## Od tąd się powtarza, zrobić coś z tym!
######################################## Od tąd się powtarza, zrobić coś z tym!

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