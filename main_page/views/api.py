# -*- coding: utf-8 -*-
from base import *
import psutil
from pyramid.response import FileResponse
@view_config(route_name='jsonp_post_comments', renderer='jsonp')
def my_view(request):
    article_id = int(request.GET['post_id'])
    comments=[]
    for position in DBSession.query(Articles_Comments).filter_by(article_id=article_id):
       username=DBSession.query(People).filter_by(id=position.author_id).first().username
       comments.append([position.id,username,str(position.add_date)[:str(position.add_date).find(".")],position.content])
    return {'comments':comments}

@view_config(route_name='jsonp_people', renderer='jsonp')
def jsonp_people(request):
    people="["
    for position in DBSession.query(People):
       people+='{"name": "%s","pesel": "%s","email": "%s","value": "%s","tokens": ["%s","%s"]},'%\
       (position.full_name,position.pesel,position.email.lower(),position.email.lower(),\
       position.first_name,position.last_name)
    people=people[:-1]+"]"
    with tempinput(people) as tempfilename:
        return FileResponse(tempfilename)

@view_config(route_name='jsonp_groups', renderer='jsonp')
def jsonp_groups(request):
    groups=[]
    for position in DBSession.query(Groups):
       groups.append(position.name)
    return {'groups':groups}
    
@view_config(route_name='jsonp_year', renderer='jsonp')
def jsonp_groups(request):
    #groups=[]#
    #for position in DBSession.query(Groups):#
    #   groups.append(position.name)#
    return {'yearname':"LOL"}

@view_config(route_name='jsonp_year_add', renderer='jsonp')
def jsonp_groups(request):
    if set(['startdate','enddate']) <= set(request.params):
        request.params['startdate']
        request.params['enddate']
        
        return {'message':"Podany rok istnieje już w bazie danych"}
    return {'message':"Podany rok istnieje już w bazie danych"}

@view_config(route_name='jsonp_mobile_login', renderer='jsonp')
def my_view4(request):
    #code = request.POST['code']
    code="UKJAASDLXCAOIW3245"
    username=[]
    groups=[]
    lessons=["","","","","","",""]
    for position in DBSession.query(People).filter_by(app_code=code):
       username.append(position.username)
       for lol in position.classes:
          for xd in DBSession.query(Groups).filter_by(id=lol.groups_id):
             groups.append(xd.name)
          for woow in DBSession.query(Lessons).filter_by(group_id=lol.groups_id).filter_by(day=1).filter_by(part_1=lol.part_1):
             lessons[int(woow.order)-1]=unicode(woow.order)+u". "+unicode(woow.teacher_subject.subject.name)+u" "+unicode(woow.teacher_subject.teacher.username)
    return {'username':username,'groups':groups,'lessons':lessons}

@view_config(route_name='jsonp_system_info', renderer='jsonp')
def jsnop_system_info(request):
    return {'cpu_times':psutil.cpu_times(),'virtual_memory':psutil.virtual_memory(),'swap_memory':psutil.swap_memory(),'disk_usage':psutil.disk_usage('/'),
    'cpu_percent':psutil.cpu_percent(interval=0.1, percpu=False)}
##########
# Users ##
##########
@view_config(route_name='user_list', renderer='jsonp')
def users_list(request):
    page={"Result":"OK","Records":[]}
    startIndex=request.params['jtStartIndex']
    sorting=request.params['jtSorting'].split(" ")
    print sorting
    query=DBSession.query(People)
    for position in query:
        page['Records'].append({"UserID":position.id,"FirstName":position.first_name,"SecondName":position.second_name,
                                "LastName":position.last_name,"Pesel":position.pesel,"BirthDate":str(position.birthdate.date()),
                                "Email":position.email,"PhoneNumber":position.phonenumber,
                                "Password":"do_not_change","Group":1})
    page['TotalRecordCount']=query.count()
    return page

@view_config(route_name='delete_user', renderer='jsonp')
def delete_user(request):
    if 'UserID' in request.params:
        try:
            session = DBSession()
            user = DBSession.query(People).filter_by(id=request.params['UserID']).first()
            if not user.email_confirmed:
                session.delete(user)
                transaction.commit()
                return {"Result":"OK"}
            else:
                return {"Result":"ERROR","Message":"Nie można usunąć użytkownika, który potwierdził swój adres email."}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"Fail"}

@view_config(route_name='update_user', renderer='jsonp')
def update_user(request):
    if set(["UserID","FirstName","SecondName","LastName","Pesel",
            "BirthDate","Email","Password","Group"]) <= set(request.params):
        try:
            session = DBSession()
            user = DBSession.query(People).filter_by(id=request.params['UserID']).first()
            user.first_name=request.params["FirstName"]
            user.second_name=request.params["FirstName"]
            user.last_name=request.params["LastName"]
            user.pesel=request.params["Pesel"]
            user.birthdate=datetime.datetime(*(time.strptime(request.params['BirthDate'], "%d.%m.%Y")[0:6]))
            user.phonenumber=request.params["PhoneNumber"]
            user.email=request.params["Email"]
            if request.params["Password"]!="do_not_change":
                user.password=hashlib.sha512(unicode(request.params["Password"]+str(user.registration_date).encode('utf-8'))).hexdigest()
            user.group_id=request.params["Group"]
            transaction.commit()
            return {"Result":"OK"}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"ERROR","Message":"Not enought data."}

@view_config(route_name='create_user', renderer='jsonp')
def create_user(request):
    page={"Result":"OK","Record":[]}
    if set(["FirstName","SecondName","LastName","Pesel","BirthDate","Email","Password","Group"]) <= set(request.params):
        try:
            session = DBSession()
            wallet = Wallet(0)
            session.add(wallet)
            session.flush()
            session.refresh(wallet)
            user = People(request.params["FirstName"], request.params["SecondName"], request.params["LastName"],
                          request.params["Pesel"],
                          datetime.datetime(*(time.strptime(request.params['BirthDate'], "%d.%m.%Y")[0:6])),
                          request.params["PhoneNumber"],request.params["Email"],request.params["Password"],
                          "","",wallet.id,0,0,0,request.params["Group"])
            session.add(user)
            page['Record'].append({"UserID":user.id,"FirstName":user.first_name,
                                    "SecondName":user.second_name,"LastName":user.last_name,
                                    "Pesel":user.pesel,"BirthDate":str(user.birthdate.date()),
                                    "Email":user.email,"PhoneNumber":user.phonenumber,
                                    "Password":"do_not_change","Group":1})
            transaction.commit()
        except DBAPIError:
            return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
        except ValueError:
            return {"Result":"ERROR","Message":"Nieprawidłowa data urodzenia :/"}
    return page
############
# Lessons ##
############
@view_config(route_name='lesson_list', renderer='jsonp')
def lesson_list(request):
    page={"Result":"OK","Records":[]}
    startIndex=request.params['jtStartIndex']
    sorting=request.params['jtSorting'].split(" ")
    print sorting
    query=DBSession.query(Lessons)
    for position in query:
        page['Records'].append({"LessonID":position.id,"Teacher":position.teacher_id,"Subject":position.subject_id,
                                "Group":position.group_id,"Room":position.room,"ModificationDate":str(position.updated.date())})
    page['TotalRecordCount']=query.count()
    return page
@view_config(route_name='delete_lesson', renderer='jsonp')
def delete_lesson(request):
    if 'LessonID' in request.params:
        session = DBSession()
        lesson = DBSession.query(Lessons).filter_by(id=request.params['LessonID']).first()
        session.delete(lesson)
        transaction.commit()
        return {"Result":"OK"}
    return {"Result":"Fail"}
@view_config(route_name='update_lesson', renderer='jsonp')
def update_lesson(request):
    if set(["LessonID","timetableID","Teacher","Group","Subject",
            "day","hour","Room"]) <= set(request.params):
        try:
            session = DBSession()
            lesson = DBSession.query(Lessons).filter_by(id=request.params['LessonID']).first()
            lesson.schedule_id=request.params["timetableID"]
            lesson.teacher_id=request.params["Teacher"]
            lesson.group_id=request.params["Group"]
            lesson.subject_id=request.params["Subject"]
            lesson.day=request.params["day"]
            lesson.order=request.params["hour"]
            lesson.room=request.params["Room"]
            transaction.commit()
            return {"Result":"OK"}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"ERROR","Message":"Not enought data."}
@view_config(route_name='create_lesson', renderer='jsonp')
def create_lesson(request):
    page={"Result":"OK"}
    if "Teacher" in request.params and "Subject" in request.params:
        #try:
        session = DBSession()
        lesson = Lessons(request.params["timetableID"], request.params["Teacher"], request.params["Group"],
                         request.params["Subject"],request.params["day"],request.params["hour"],request.params["Room"])
        session.add(lesson)
        #except LOL:
         #   return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
        page["Record"]={"LessonID":lesson.id ,"Teacher":2,"Subject":7,"Group":1,"Room":112}
        transaction.commit()
    return page

    return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
###############
# Timetables ##
###############
@view_config(route_name='timetable_list', renderer='jsonp')
def timetable(request):
    page={"Result":"OK","Records":[]}
    startIndex=request.params['jtStartIndex']
    sorting=request.params['jtSorting'].split(" ")
    print sorting
    query=DBSession.query(Schedules)
    for position in query:
        page['Records'].append({"TimetableId":position.id,"Start":str(position.start),"End":str(position.end),"ModificationDate":str(position.updated.date())})
    page['TotalRecordCount']=query.count()
    return page

@view_config(route_name='delete_timetable', renderer='jsonp')
def delete_timetable(request):
    if 'TimetableId' in request.params:
        session = DBSession()
        schedule = DBSession.query(Schedules).filter_by(id=request.params['TimetableId']).first()
        session.delete(schedule)
        transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='update_timetable', renderer='jsonp')
def update_timetable(request):
    if "Start" in request.params and "End" in request.params and 'TimetableId' in request.params:
        session = DBSession()
        schedule = DBSession.query(Schedules).filter_by(id=request.params['TimetableId']).first()
        schedule.start=datetime.datetime(*(time.strptime(request.params['Start'], "%d.%m.%Y")[0:6]))
        schedule.end=datetime.datetime(*(time.strptime(request.params['End'], "%d.%m.%Y")[0:6]))
        transaction.commit()
        return {"Result":"OK"}
    return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}

@view_config(route_name='create_timetable', renderer='jsonp')
def create_timetable(request):
    page={"Result":"OK"}
    if "Start" in request.params and "End" in request.params:
        #try:
        session = DBSession()
        start=datetime.datetime(*(time.strptime(request.params['Start'], "%d.%m.%Y")[0:6]))
        end=datetime.datetime(*(time.strptime(request.params['End'], "%d.%m.%Y")[0:6]))
        schedule = Schedules(start,end)
        session.add(schedule)

        #except LOL:
         #   return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
        page["Record"]={"TimetableId":schedule.id,"Start":str(schedule.start),"End":str(schedule.end),"ModificationDate":str(schedule.updated.date())}
        transaction.commit()
    return page



@view_config(route_name='options_teacher_list', renderer='jsonp')
def options_teacher_list(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(Teachers):
        page['Options'].append({"DisplayText":position.user.full_name,"Value":position.user.id})
    return page

@view_config(route_name='options_subjects_list', renderer='jsonp')
def options_subjects_list(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(Subjects):
        page['Options'].append({"DisplayText":position.name,"Value":position.id})
    return page

@view_config(route_name='options_groups_list', renderer='jsonp')
def options_groups_list(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(Divisions):
        page['Options'].append({"DisplayText":position.name,"Value":position.id})
    return page


##########
# Folders ##
##########
@view_config(route_name='folder_list', renderer='jsonp')
def folder_list(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    page={"Result":"OK","Records":[]}
    startIndex=request.params['jtStartIndex']
    sorting=request.params['jtSorting'].split(" ")
    user = DBSession.query(People).filter_by(email=logged_in).first()
    query=DBSession.query(Folders).filter_by(user_id=user.id).filter_by(deleted=False)
    for position in query:
        folder_data = DBSession.query(FoldersVersions).filter_by(folder_id=position.id).order_by('-id').first()
        try:
            page['Records'].append({"FolderID":position.id,"Title":folder_data.title,
                                    "Tags":folder_data.tags,"CSS":folder_data.css_id,
                                    "GPG":position.sign,"Published":str(position.state)})
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś jest nie tak :/"}
    page['TotalRecordCount']=query.count()
    return page

@view_config(route_name='delete_folder', renderer='jsonp')
def delete_folder(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    if 'FolderID' in request.params:
        try:
            session = DBSession()
            user = DBSession.query(People).filter_by(email=logged_in).first()
            folder = DBSession.query(Folders).filter_by(id=request.params['FolderID']).first()
            if folder.user.id == user.id:
                folder.deleted = True
                transaction.commit()
                return {"Result":"OK"}
            else:
                return {"Result":"ERROR","Message":"Ten folder nie należy do Ciebie. Nie możesz go usunąć."}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"Fail"}

@view_config(route_name='update_folder', renderer='jsonp')
def update_folder(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    if set(["Title","Tags","CSS","GPG","Published"]) <= set(request.params):
        try:
            session = DBSession()
            folder = DBSession.query(Folders).filter_by(id=request.params['FolderID']).first()
            folder_data = FoldersVersions(folder.id, request.params["Title"], request.params["Tags"],
                                          request.params["CSS"])
            folder.state={'True':True,'False':False}[request.params["Published"]]
            folder.sign=request.params["GPG"]
            session.add(folder_data)
            transaction.commit()
            return {"Result":"OK"}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"ERROR","Message":"Not enought data."}

@view_config(route_name='create_folder', renderer='jsonp')
def create_folder(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    page={"Result":"OK","Record":[]}
    if set(["Title","Tags","CSS","GPG","Published"]) <= set(request.params):
        try:
            session = DBSession()
            user = DBSession.query(People).filter_by(email=logged_in).first()
            folder = Folders(user.id)
            session.add(folder)
            session.flush()
            session.refresh(folder)
            folder_data = FoldersVersions(folder.id, request.params["Title"], request.params["Tags"],
                                          request.params["CSS"])
            folder.state={'True':True,'False':False}[request.params["Published"]]
            folder.sign=request.params["GPG"]
            session.add(folder_data)
            page['Record'].append({"FolderID":folder_data.id,"Title":folder_data.title,
                                    "Tags":folder_data.tags,"CSS":folder_data.css_id,
                                    "GPG":folder.sign})
            transaction.commit()
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return page

@view_config(route_name='options_folders_list', renderer='jsonp')
def options_folders_list(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(Folders):
        page['Options'].append({"DisplayText":position.last_version.title,"Value":position.id})
    return page

############
# Entries ##
############
@view_config(route_name='entry_list', renderer='jsonp')
def entry_list(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    page={"Result":"OK","Records":[]}
    startIndex=request.params['jtStartIndex']
    sorting=request.params['jtSorting'].split(" ")
    user = DBSession.query(People).filter_by(email=logged_in).first()
    query = DBSession.query(Entries).filter_by(user_id=user.id).filter_by(deleted=False)
    for position in query:
        entry_data = position.last_version
        try:
            page['Records'].append({"EntryID":position.id, "FolderID":entry_data.entry.folder.id, "Title":entry_data.title,
                                    "Tags":entry_data.tags,"CSS":entry_data.css_id,"Published":str(position.state)})
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś jest nie tak :/"}
    page['TotalRecordCount']=query.count()
    return page

@view_config(route_name='delete_entry', renderer='jsonp')
def delete_entry(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    if 'FolderID' in request.params:
        try:
            session = DBSession()
            user = DBSession.query(People).filter_by(email=logged_in).first()
            folder = DBSession.query(Folders).filter_by(id=request.params['FolderID']).first()
            if folder.user.id == user.id:
                folder.deleted = True
                transaction.commit()
                return {"Result":"OK"}
            else:
                return {"Result":"ERROR","Message":"Ten folder nie należy do Ciebie. Nie możesz go usunąć."}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"Fail"}

@view_config(route_name='update_entry', renderer='jsonp')
def update_entry(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    if set(["Title","Tags","CSS","GPG","Published"]) <= set(request.params):
        try:
            session = DBSession()
            folder = DBSession.query(Folders).filter_by(id=request.params['FolderID']).first()
            folder_data = FoldersVersions(folder.id, request.params["Title"], request.params["Tags"],
                                          request.params["CSS"])
            folder.state={'True':True,'False':False}[request.params["Published"]]
            folder.sign=request.params["GPG"]
            session.add(folder_data)
            transaction.commit()
            return {"Result":"OK"}
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return {"Result":"ERROR","Message":"Not enought data."}

@view_config(route_name='create_entry', renderer='jsonp')
def create_entry(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    page={"Result":"OK","Record":[]}
    if set(["FolderID","Title","Tags","CSS","Published"]) <= set(request.params):
        try:
            session = DBSession()
            user = DBSession.query(People).filter_by(email=logged_in).first()
            entry = Entries(user.id,request.params["FolderID"])
            session.add(entry)
            session.flush()
            session.refresh(entry)
            entry_data = EntriesVersions(entry.id, request.params["Title"],u"",request.params["Tags"],request.params["CSS"])
            entry.state={'True':True,'False':False}[request.params["Published"]]
            session.add(entry_data)
            page['Record'].append({"EntryID":entry.id, "FolderID":entry.folder_id, "Title":entry_data.title,
                                    "Tags":entry_data.tags,"CSS":entry_data.css_id,"Published":str(entry.state)})
            transaction.commit()
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    return page