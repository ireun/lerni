# -*- coding: utf-8 -*-
from base import *

@view_config(route_name='view_home')
def my_view(request):
    return HTTPFound(location = request.route_url('home', page_number ='1'))
        
@view_config(route_name='home', renderer='main.mak')
def my_view3(request):
    breadcrumbs=[]
    try:
        page_num = int(request.matchdict['page_number'])
    except:
        raise exception_response(404)
    editor=0
    if has_permission('edit_articles', request.context, request):
        editor=1
    logged_in = authenticated_userid(request)
    try:
        menu_top_list =[]
        for position in DBSession.query(MenuTop):
            menu_top_list.append([position.link,position.name])
        menu_left_list =[]
        for position in DBSession.query(MenuLeft):
            menu_left_list.append([position.link,position.name])
            articles = []
            app = 3 #articles per page
            tnoa = DBSession.query(Articles).count() #total_number_of_aritcles
            if not app*page_num-tnoa<app:                                        ## Tutaj może być jakiś błąd, zastanowić się, czy _napewno_ działa!
                return HTTPFound(location = request.route_url('home', page_number = int(ceil(float(tnoa)/float(app)))))
                
        for position in DBSession.query(Articles).filter(Articles.state==True).order_by(desc(Articles.add_date)).order_by(Articles.sticked):
            username=DBSession.query(People).filter_by(id=position.author_id).first().username
            comments_num = DBSession.query(Articles_Comments).filter_by(article_id=position.id).count()
            
            position2 = DBSession.query(ArticlesContent).filter_by(id=position.id).order_by(desc(ArticlesContent.id)).first()
            articles.append([position.id,position2.title,str(position.add_date)[:str(position.add_date).find(".")],username,position2.content,comments_num])
        #for position in DBSession.query(Articles).filter(Articles.id<tnoa-(page_num-1)*app+1, Articles.id>tnoa-page_num*app).order_by(desc(Articles.id)):
        #    username = DBSession.query(People).filter_by(id=position.author_id).first().username
        #   	comments_num = DBSession.query(Articles_Comments).filter_by(article_id=position.id).count()
        #    articles.append([position.id,position.title,str(position.add_date)[:str(position.add_date).find(".")],username,position.content,comments_num])
        #text=u""
        #for position in DBSession.query(Groups):
        #   text=text+unicode(position.id)+". "+unicode(position.name)+"<br />"
        #for position in DBSession.query(Lessons).filter_by(group_id=16).order_by(Lessons.day): ## dodać sortowanie wg. godzin .order_by(Lessons.order)
        #	text=text+unicode(position.id)+[u"pon",u"wt",u"śr",u"czw",u"pt"][position.day]+u" "+unicode(position.order)+u" "+unicode(position.group.name)+u" "
        #	text=text+unicode(position.teacher_subject.subject.name)+u" "+unicode(position.teacher_subject.teacher.username)+u"<br />"
        #articles.append(["","","","",text,0])
        name=""
        if logged_in:
            name=DBSession.query(People).filter_by(login=logged_in).first().username
    except DBAPIError:
        return Response("SQL ERROR", content_type='text/plain', status_int=500)
    return {'menu_top_list':menu_top_list, 'menu_left_list':menu_left_list, 'articles':articles, 'logged_in':logged_in, 'editor':editor, 'name':name, 'breadcrumbs':breadcrumbs, 'allerts':''}

@view_config(route_name='plan')#, renderer='plan.mak')
def my_view4(request):
    #for position in DBSession.query(TeacherSubject):
    #   	text=text+unicode(position.id)+u". "+unicode(DBSession.query(People).filter_by(id=position.teacher_id).first().username)+" - "+unicode(DBSession.query(Subjects).filter_by(id=position.subject_id).first().name)+"<br />"
    #   for position in DBSession.query(Groups):
    #      text=text+unicode(position.id)+". "+unicode(position.name)+"<br />"
    #   articles.append(["","","","",text,0])
    #text=u""
    #for position in DBSession.query(Groups):
    #   text=text+unicode(position.name)+u"\n"
    #   lessons=[[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]],[[],[]]]
    #   text=text+u"Poniedzialek\n"
    #   for position2 in DBSession.query(Lessons).filter_by(group_id=position.id).filter_by(day=0).order_by(Lessons.order):
    #      subject_id=DBSession.query(TeacherSubject).filter_by(id=position2.teacher_subject_id).first().subject_id
    #      subject_name=DBSession.query(Subjects).filter_by(id=subject_id).first().name
    #      #text=text+unicode(position2.order)+unicode(subject_name)+u"\n"
    #      if position2.part_1==1:
    #         lessons[position2.order][0]=unicode(subject_name)
    #      if position2.part_2==1:
    #         lessons[position2.order][1]=unicode(subject_name)
    #   for x in lessons:
    #      text=text+u" "+unicode(x[0])+u"/"+unicode(x[1])+u"\n"
    #   text=text+u"Wtorek\n"
    #   for position2 in DBSession.query(Lessons).filter_by(group_id=position.id).filter_by(day=1).order_by(Lessons.order):
    #      subject_id=DBSession.query(TeacherSubject).filter_by(id=position2.teacher_subject_id).first().subject_id
    #      subject_name=DBSession.query(Subjects).filter_by(id=subject_id).first().name
    #      #text=text+unicode(position2.order)+unicode(subject_name)+u"\n"
    #      if position2.part_1==1:
    #         lessons[position2.order][0]=unicode(subject_name)
    #      if position2.part_2==1:
    #         lessons[position2.order][1]=unicode(subject_name)
    #   for x in lessons:
    #      text=text+u" "+unicode(x[0])+u"/"+unicode(x[1])+u"\n"
    #   text=text+u"Sroda\n"
    #   for position2 in DBSession.query(Lessons).filter_by(group_id=position.id).filter_by(day=2).order_by(Lessons.order):
    #      subject_id=DBSession.query(TeacherSubject).filter_by(id=position2.teacher_subject_id).first().subject_id
    #      subject_name=DBSession.query(Subjects).filter_by(id=subject_id).first().name
    #      #text=text+unicode(position2.order)+unicode(subject_name)+u"\n"
    #      if position2.part_1==1:
    #         lessons[position2.order][0]=unicode(subject_name)
    #      if position2.part_2==1:
    #         lessons[position2.order][1]=unicode(subject_name)
    #   for x in lessons:
    #      text=text+u" "+unicode(x[0])+u"/"+unicode(x[1])+u"\n"
    #   text=text+u"Czwartek\n"
    #   for position2 in DBSession.query(Lessons).filter_by(group_id=position.id).filter_by(day=3).order_by(Lessons.order):
    #      subject_id=DBSession.query(TeacherSubject).filter_by(id=position2.teacher_subject_id).first().subject_id
    #      subject_name=DBSession.query(Subjects).filter_by(id=subject_id).first().name
    #      #text=text+unicode(position2.order)+unicode(subject_name)+u"\n"
    #      if position2.part_1==1:
    #         lessons[position2.order][0]=unicode(subject_name)
    #      if position2.part_2==1:
    #         lessons[position2.order][1]=unicode(subject_name)
    #   for x in lessons:
    #      text=text+u" "+unicode(x[0])+u"/"+unicode(x[1])+u"\n"
    #   text=text+u"Piatek\n"
    #   for position2 in DBSession.query(Lessons).filter_by(group_id=position.id).filter_by(day=4).order_by(Lessons.order):
    #      subject_id=DBSession.query(TeacherSubject).filter_by(id=position2.teacher_subject_id).first().subject_id
    #      subject_name=DBSession.query(Subjects).filter_by(id=subject_id).first().name
    #      #text=text+unicode(position2.order)+unicode(subject_name)+u"\n"
    #      if position2.part_1==1:
    #         lessons[position2.order][0]=unicode(subject_name)
    #      if position2.part_2==1:
    #         lessons[position2.order][1]=unicode(subject_name)
    #   for x in lessons:
    #      text=text+u" "+unicode(x[0])+u"/"+unicode(x[1])+u"\n"
    return Response(body="text", content_type='text/plain')













