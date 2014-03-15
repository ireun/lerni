# -*- coding: utf-8 -*-
from base import *
import psutil
from pyramid.security import authenticated_userid
import datetime

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.competitions.nameList'])
def api_jsonp_lerni_competitors_competitions_getlist(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(CompetitorsCompetitions):
        page['Options'].append({"DisplayText":position.name,"Value":position.id})
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.groups.nameList'])
def api_jsonp_lerni_competitors_groups_getlist(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(CompetitorsGroups):
        page['Options'].append({"DisplayText":position.name,"Value":position.id})
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.types.nameList'])
def api_jsonp_lerni_competitors_types_getlist(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(CompetitorsTypes):
        page['Options'].append({"DisplayText": position.name,"Value": position.id})
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.subjects.nameList'])
def api_jsonp_lerni_subjects_namelist(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(Subjects):
        page['Options'].append({"DisplayText": position.name,"Value": position.id})
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.tutors.nameList'])
def api_jsonp_lerni_competitors_tutors_getlist(request):
    page={"Result":"OK","Options":[]}
    for position in DBSession.query(CompetitorsTutors):
        page['Options'].append({"DisplayText": position.name,"Value": position.id})
    return page
#################
# Graduates   #
#################
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.graduates.getList',
                                                                'jtStartIndex','jtPageSize'])
def jsonp_graduates_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")

    query = DBSession.query(Graduates)
    query = query.order_by(eval("Graduates."+sorting[0]+{"ASC": ".asc()", "DESC":".desc()"}[sorting[1]]))
    if "name" in request.params:
        names = request.params['name'].split(" ")
        for name in names:
            query = query.filter(or_(Graduates.name.like("%"+name+"%"),
                                     Graduates.graduation.like("%"+name+"%"),
                                     Graduates.about.like("%"+name+"%")))
    page['TotalRecordCount'] = query.count()
    query = query.offset(int(start_index)).limit(int(page_size))

    for position in query:
        page['Records'].append({u"id": position.id,
                                u"name": position.name,
                                u"graduation": position.graduation,
                                u"about": position.about})
    return page


#################
# Competitors   #
#################
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.getList',
                                                                'jtStartIndex','jtPageSize'])
def jsonp_competitors_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")

    query = DBSession.query(Competitors).join(CompetitorsCompetitions).join(Subjects).join(CompetitorsGroups)\
        .join(CompetitorsTypes).join(CompetitorsTutors)
    if sorting[0]=="year": sorting[0]="start_year"
    if sorting[0]=="subject_id" and sorting[1]=="DESC":
        query = query.order_by(Subjects.name.desc())
    elif sorting[0]=="subject_id" and sorting[1]=="ASC":
        query = query.order_by(Subjects.name.asc())
    else:
        query = query.order_by(eval("Competitors."+sorting[0]+{"ASC": ".asc()", "DESC":".desc()"}[sorting[1]]))
    if "competitionGroupId" in request.params:
        query = query.filter(CompetitorsGroups.name.in_([request.params['competitionGroupId']]))
    if "name" in request.params:
        names = request.params['name'].split(" ")
        for name in names:
            query = query.filter(or_(Competitors.first_name.like("%"+name+"%"),
                                     Competitors.last_name.like("%"+name+"%"),
                                     CompetitorsCompetitions.name.like("%"+name+"%"),
                                     CompetitorsTypes.name.like("%"+name+"%"),
                                     CompetitorsTutors.name.like("%"+name+"%"),
                                     Subjects.name.like("%"+name+"%"), Competitors.start_year.like("%"+name+"%"),
                                     Competitors.end_year.like("%"+name+"%")))
    page['TotalRecordCount'] = query.count()
    query = query.offset(int(start_index)).limit(int(page_size))

    for position in query:
        page['Records'].append({u"id": position.id,
                                u"first_name": position.first_name,
                                u"last_name": position.last_name,
                                u"competition_group_id": position.competition_group_id,
                                u"competition_id": position.competition_id,
                                u"competitor_type_id": position.competitor_type_id,
                                u"subject_id": position.competition.subject_id,
                                u"competitor_tutor_id": position.competitor_tutor_id,
                                u"year": str(position.start_year)+"/"+str(position.end_year),
                                u"group": 1})
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.delete',
                                                                'competitor_id'])
def jsonp_competitors_delete(request):
    session = DBSession()
    competitor = DBSession.query(Competitors).filter_by(id=request.params['competitor_id']).first()
    if not competitor:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    else:
        session.delete(competitor)
        transaction.commit()
        return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.edit',
                                                                'competitor_id'])
def jsonp_competitors_edit(request):
    session = DBSession()
    competitor = DBSession.query(Competitors).filter_by(id=request.params['competitor_id']).first()
    if not competitor:
        return {"Result": "ERROR", "Message": "Coś poszło nie tak :/"}
    competitor.first_name = request.params["first_name"]
    competitor.last_name = request.params["last_name"]
    competitor.competition_group_id = request.params["competition_group_id"]
    competitor.competition_id = request.params["competition_id"]
    competitor.competitor_type_id = request.params["competitor_type_id"]
    competitor.competition_subject_id = request.params["subject_id"]
    competitor.competitor_tutor_id = request.params["competitor_tutor_id"]
    competitor.year = request.params["year"]
    transaction.commit()
    return {"Result":"OK"}
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitors.add',
                                                                'first_name'])
def jsonp_competitors_create(request):
    page={"Result": "OK", "Record": []}
    try:
        session = DBSession()
        competitor = Competitors(request.params["first_name"], request.params["last_name"],
                      request.params["competition_id"], request.params["subject_id"],
                      request.params["competitor_type_id"], request.params["year"], str(int(request.params["year"])+1),
                      request.params["competitor_tutor_id"], request.params["competition_group_id"])
        session.add(competitor)
        page['Record'].append({u"competitor_id": competitor.id,
                               u"first_name": competitor.first_name,
                               u"last_name": competitor.last_name,
                               u"competition_group_id": competitor.competition_group_id,
                               u"competition_id": competitor.competition_id,
                               u"competitor_type_id": competitor.competitor_type_id,
                               u"subject_id": competitor.competition_subject_id,
                               u"competitor_tutor_id": competitor.competitor_tutor_id,
                               u"year": competitor.start_year,
                               u"group": 1})
        transaction.commit()
    except DBAPIError:
        return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
    except ValueError:
        return {"Result":"ERROR","Message":"Nieprawidłowa data urodzenia :/"}
    return page

#################
# Competitions  #
#################
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitions.getList',
                                                                'jtStartIndex','jtPageSize'])
def jsonp_competitions_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    query = DBSession.query(CompetitorsCompetitions).order_by(CompetitorsCompetitions.id.desc()).offset(int(start_index)).limit(int(page_size))
    for position in query:
        page['Records'].append({u"competition_id": position.id,
                                u"name": position.name,
                                u"subject_id": position.subject_id})
    page['TotalRecordCount'] = DBSession.query(CompetitorsCompetitions).count()
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitions.delete',
                                                                'competition_id'])
def jsonp_competitions_delete(request):
    session = DBSession()
    competition = DBSession.query(CompetitorsCompetitions).filter_by(id=request.params['competition_id']).first()
    if not competitor:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    else:
        session.delete(competition)
        transaction.commit()
        return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitions.edit',
                                                                'competition_id'])
def jsonp_competitions_edit(request):
    session = DBSession()
    competition = DBSession.query(CompetitorsCompetitions).filter_by(id=request.params['competition_id']).first()
    if not competition:
        return {"Result": "ERROR", "Message": "Coś poszło nie tak :/"}
    competition.name = request.params["name"]
    competition.subject_id = request.params["subject_id"]
    transaction.commit()
    return {"Result":"OK"}
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.competitions.add',
                                                                'first_name'])
def jsonp_competitions_create(request):
    page={"Result": "OK", "Record": []}
    try:
        session = DBSession()
        competition = Competitors(request.params["name"], request.params["subject_id"])
        session.add(competition)
        page['Record'].append({u"competition_id": competition.id,
                               u"first_name": competition.name,
                               u"subject_id": competition.subject_id})
        transaction.commit()
    except DBAPIError:
        return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
    return page

def get_week(day):
    start = day-datetime.timedelta(day.weekday())
    end = day+datetime.timedelta(6-day.weekday())
    return start, end

#################
# Lucky Numbers #
#################
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.lucky.getList',
                                                                'jtStartIndex','jtPageSize'])
def jsonp_lucky_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = int(request.params['jtStartIndex'])
    page_size = int(request.params['jtPageSize'])
    for x in range(page_size):
        week = get_week(datetime.datetime.now().date()+datetime.timedelta(1-7*(start_index+x)+7))
        query = DBSession.query(LuckyNumbers).filter(LuckyNumbers.date.between(week[0], week[1]))
        record = dict([('first_date', 0), ('0', ""), ('1', ""), ('2', ""), ('3', ""), ('4', ""), ('5', ""), ('6', ""),
                      ('start', ""), ('end', "")])
        record['first_date'] = str(week[0])
        record['start'] = str(week[0])
        record['end'] = str(week[1])
        for position in query:
            record[str(position.date.weekday())] = position.number
        page['Records'].append(record)
    page['TotalRecordCount'] = 1000
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.lucky.delete',
                                                                'first_date'])
def jsonp_lucky_delete(request):
    session = DBSession()
    date = datetime.datetime(*(time.strptime(request.params['first_date'], "%Y-%m-%d")[0:6])).date()
    week = get_week(date+datetime.timedelta(1))
    query = DBSession.query(LuckyNumbers).filter(LuckyNumbers.date.between(week[0], week[1]))
    for x in query:
        session.delete(x)
    transaction.commit()
    return {"Result":"OK"}


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.lucky.edit',
                                                                'first_date', '0', '1', '2', '3', '4', '5', '6'])
def jsonp_lucky_edit(request):
    session = DBSession()
    date = datetime.datetime(*(time.strptime(request.params['first_date'], "%Y-%m-%d")[0:6])).date()
    week = get_week(date+datetime.timedelta(1))
    for x in range(7):
        date2 = week[0]+datetime.timedelta(x)
        number = DBSession.query(LuckyNumbers).filter_by(date=date2).first()
        if number and request.params[str(x)]:
            number.number = request.params[str(x)]
        elif number and not request.params[str(x)]:
            session.delete(number)
        elif request.params[str(x)]:
            number = LuckyNumbers(date2,request.params[str(x)])
            session.add(number)
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.lucky.add', 'first_date'])
def jsonp_lucky_create(request):
    page={"Result":"OK","Record":{}}
    session = DBSession()
    date = datetime.datetime(*(time.strptime(request.params['first_date'], "%Y-%m-%d")[0:6])).date()
    week = get_week(date+datetime.timedelta(1))
    record = {"first_date": str(week[0]), "0": " ", "1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ",
              "start" : str(week[0]), "end" : str(week[1])}
    for x in range(7):
        date2 = week[0]+datetime.timedelta(x)
        number = DBSession.query(LuckyNumbers).filter_by(date=date2).first()
        if number:
            number.number = request.params[str(x)]
        elif number and not request.params[str(x)]:
            session.delete(number)
        elif request.params[str(x)]:
            number = LuckyNumbers(date2, request.params[str(x)])
            session.add(number)
        record[str(x)]=request.params[str(x)]
    transaction.commit()
    page['Record'] = record
    return page
################
################
################
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
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.users.getList'])
def api_jsonp_lerni_users_getlist(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    print sorting
    query = DBSession.query(People).offset(int(start_index)).limit(int(page_size))
    for position in query:
        page['Records'].append({u"user_id": position.id,
                                u"first_name": position.first_name,
                                u"second_name": position.second_name,
                                u"last_name": position.last_name,
                                u"pesel": position.pesel,
                                u"phone_number": position.phone_number,
                                u"birth_date": str(position.birth_date.date()),
                                u"email": position.email,
                                u"password": "do_not_change",
                                u"group": 1})
    page['TotalRecordCount'] = DBSession.query(People).count()
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.users.delete','user_id'])
def api_jsonp_lerni_users_delete(request):
    session = DBSession()
    user = DBSession.query(People).filter_by(id=request.params['user_id']).first()
    if not user:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    elif not user.email_confirmed:
        session.delete(user)
        transaction.commit()
        return {"Result":"OK"}
    else:
        return {"Result": "ERROR", "Message": "Nie można usunąć użytkownika, który potwierdził swój adres email."}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.users.edit',
                                                                "user_id", "first_name", "second_name", "last_name",
                                                                "pesel", "birth_date", "email", "password", "group"])
def api_jsonp_lerni_users_edit(request):
    session = DBSession()
    user = DBSession.query(People).filter_by(id=request.params['user_id']).first()
    if not user:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    user.first_name = request.params["first_name"]
    user.second_name = request.params["second_name"]
    user.last_name = request.params["last_name"]
    user.pesel = request.params["pesel"]
    user.birth_date = datetime.datetime(*(time.strptime(request.params['birth_date'], "%Y-%m-%d")[0:6]))
    user.phone_number = request.params["phone_number"]
    user.email = request.params["email"]
    if request.params["password"] != "do_not_change":
        user.password = hashlib.sha512(unicode(request.params["password"]+
                                               str(user.registration_date).encode('utf-8'))).hexdigest()
    user.group_id = request.params["group"]
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp','method=lerni.users.add',
            "first_name", "second_name", "last_name", "pesel", "birth_date", "email", "password", "group"])
def api_jsonp_lerni_users_add(request):
    page={"Result":"OK","Record":[]}
    try:
        session = DBSession()
        wallet = Wallet(0)
        session.add(wallet)
        session.flush()
        session.refresh(wallet)
        user = People(request.params["first_name"], request.params["second_name"], request.params["last_name"],
                      request.params["pesel"],
                      datetime.datetime(*(time.strptime(request.params['birth_date'], "%Y-%m-%d")[0:6])),
                      request.params["phone_number"],request.params["email"],request.params["password"],
                      "","",wallet.id,0,0,0,request.params["group"])
        session.add(user)
        page['Record'].append({"user_id":user.id,"first_name":user.first_name,
                                "second_name":user.second_name,"last_name":user.last_name,
                                "pesel":user.pesel,"birth_date":str(user.birth_date.date()),
                                "email":user.email,"phone_number":user.phone_number,
                                "password":"do_not_change","group":1})
        transaction.commit()
    except DBAPIError:
        return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
    except ValueError:
        return {"Result":"ERROR","Message":"Nieprawidłowa data urodzenia :/"}
    return page

############
# Lessons ##
############
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.lessons.getList',
            'timetable_id', 'day', 'hour', 'jtStartIndex','jtPageSize', 'jtSorting'])
def jsonp_lessons_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    schedule_id = request.params['timetable_id']
    day = request.params['day']
    hour = request.params['hour']
    print sorting
    query = DBSession.query(Lessons).filter_by(schedule_id=schedule_id).filter_by(day=day).filter_by(order=hour).\
        offset(int(start_index)).limit(int(page_size))
    for lesson in query:
        groups = []
        for lesson_group in DBSession.query(LessonsGroups).filter_by(lesson=lesson):
            groups.append(lesson_group.group.name)
        page['Records'].append({"lesson_id": lesson.id,
                                "teacher": lesson.teacher_id,
                                "subject": lesson.subject_id,
                                "group": "; ".join(groups),
                                "room": lesson.room,
                                "modification_date": str(lesson.updated.date())})
    page['TotalRecordCount'] = DBSession.query(Lessons).filter_by(schedule_id=schedule_id).filter_by(day=day).\
        filter_by(order=hour).count()
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
             'method=lerni.timetables.lessons.delete', 'lesson_id'])
def jsonp_lessons_delete(request):
    session = DBSession()
    lesson = DBSession.query(Lessons).filter_by(id=request.params['lesson_id']).first()
    if not lesson:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    session.delete(lesson)
    transaction.commit()
    return {"Result":"OK"}


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.lessons.edit', 'timetable_id', 'day', 'hour'])
def jsonp_lessons_update(request):
    session = DBSession()
    lesson = DBSession.query(Lessons).filter_by(id=request.params['lesson_id']).first()
    if not lesson:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    lesson.schedule_id=request.params["timetable_id"]
    lesson.teacher_id=request.params["teacher"]
    lesson.subject_id=request.params["subject"]
    lesson.day=request.params["day"]
    lesson.order=request.params["hour"]
    lesson.room=request.params["room"]
    transaction.commit()
    return {"Result":"OK"}


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.lessons.edit', 'timetable_id', 'teacher', 'subject', 'day', 'hour', 'room'])
def jsonp_lessons_create(request):
    page={"Result":"OK"}
    session = DBSession()
    lesson = Lessons(request.params["timetable_id"],
                     request.params["teacher"],
                     request.params["subject"],
                     request.params["day"],
                     request.params["hour"],
                     request.params["room"])
    session.add(lesson)
    page["Record"]={"lesson_id": lesson.id,
                    "teacher": lesson.teacher_id,
                    "subject": lesson.subject_id,
                    "group": "lesson.groups", #fuck
                    "room": lesson.room}
    transaction.commit()
    return page
###############
# Timetables ##
###############
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.getList', 'jtStartIndex','jtPageSize', 'jtSorting'])
def jsonp_timetables_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    print sorting
    query = DBSession.query(Schedules).offset(int(start_index)).limit(int(page_size))
    for position in query:
        page['Records'].append({"timetable_id": position.id,
                                "start": str(position.start),
                                "end": str(position.end),
                                "modification_date": str(position.updated.date())
                                })
    page['TotalRecordCount'] = DBSession.query(Schedules).count()
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.delete', 'timetable_id'])
def jsonp_timetables_delete(request):
    session = DBSession()
    schedule = DBSession.query(Schedules).filter_by(id=request.params['timetable_id']).first()
    session.delete(schedule)
    transaction.commit()


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.edit', 'timetable_id', 'start', 'end'])
def jsonp_timetables_edit(request):
    session = DBSession()
    schedule = DBSession.query(Schedules).filter_by(id=request.params['timetable_id']).first()
    schedule.start=datetime.datetime(*(time.strptime(request.params['start'], "%Y-%m-%d")[0:6]))
    schedule.end=datetime.datetime(*(time.strptime(request.params['end'], "%Y-%m-%d")[0:6]))
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.timetables.add', 'start', 'end'])
def jsonp_timetables_create(request):
    page={"Result":"OK"}
    session = DBSession()
    start=datetime.datetime(*(time.strptime(request.params['start'], "%Y-%m-%d")[0:6]))
    end=datetime.datetime(*(time.strptime(request.params['end'], "%Y-%m-%d")[0:6]))
    schedule = Schedules(start,end)
    session.add(schedule)
    page["Record"]={"timetable_id": schedule.id,
                    "start": str(schedule.start),
                    "end": str(schedule.end),
                    "modification_date":str(schedule.updated.date())
                    }
    transaction.commit()
    return page
#############
# Subjects ##
#############
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.subjects.getList', 'jtStartIndex','jtPageSize', 'jtSorting'])
def jsonp_subjects_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    print sorting
    query = DBSession.query(Subjects).offset(int(start_index)).limit(int(page_size))
    for position in query:
        page['Records'].append({"subject_id": position.id,
                                "name": unicode(position.name),
                                "short": unicode(position.short),
                                "modification_date": unicode(position.modification_date).split(" ")[0]
                                })
    page['TotalRecordCount'] = DBSession.query(Subjects).count()
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.subjects.delete', 'subject_id'])
def jsonp_subjects_delete(request):
    session = DBSession()
    year = DBSession.query(Subjects).filter_by(id=request.params['subject_id']).first()
    session.delete(year)
    transaction.commit()
    return {"Result":"OK"}


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.subjects.edit', 'year_id', 'short', 'name'])
def jsonp_subjects_edit(request):
    session = DBSession()
    subject = DBSession.query(Subjects).filter_by(id=request.params['year_id']).first()
    subject.name = request.params['name']
    subject.short = request.params['short']
    subject.modification_date = datetime.datetime.now()
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.years.add', 'start', 'end'])
def jsonp_years_create(request):
    page={"Result":"OK"}
    session = DBSession()
    name = request.params['name']
    short = request.params['short']
    subject = SchoolYears(name, short)
    session.add(subject)
    session.flush()
    page["Record"]={"subject_id": subject.id,
                    "name": str(subject.start),
                    "short": str(subject.end),
                    "modification_date":str(subject.modification_date).split(" ")[0]
                    }
    transaction.commit()
    return page

#############
# Subjects ##
#############
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.divisions.categories.getList', 'jtStartIndex','jtPageSize', 'jtSorting'])
def jsonp_divisions_categories_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    print sorting
    query = DBSession.query(DivisionsCategories).offset(int(start_index)).limit(int(page_size))
    for position in query:
        page['Records'].append({"division_category_id": position.id,
                                "name": unicode(position.name),
                                "short": unicode(position.short),
                                "modification_date": unicode(position.modification_date).split(" ")[0]
                                })
    page['TotalRecordCount'] = DBSession.query(DivisionsCategories).count()
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.divisions.categories.delete', 'subject_id'])
def jsonp_divisions_categories_delete(request):
    session = DBSession()
    year = DBSession.query(DivisionsCategories).filter_by(id=request.params['subject_id']).first()
    session.delete(year)
    transaction.commit()
    return {"Result":"OK"}


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.divisions.categories.edit', 'year_id', 'name', 'short'])
def jsonp_divisions_categories_edit(request):
    session = DBSession()
    subject = DBSession.query(DivisionsCategories).filter_by(id=request.params['year_id']).first()
    subject.name = request.params['name']
    subject.short = request.params['short']
    subject.modification_date = datetime.datetime.now()
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.divisions.categories.add', 'name', 'short'])
def jsonp_divisions_categories_create(request):
    page={"Result":"OK"}
    session = DBSession()
    name = request.params['name']
    short = request.params['short']
    d_category = DivisionsCategories(name, short)
    session.add(d_category)
    session.flush()
    page["Record"]={"subject_id": d_category.id,
                    "name": unicode(d_category.name),
                    "short": unicode(d_category.short),
                    "modification_date":str(d_category.modification_date).split(" ")[0]
                    }
    transaction.commit()
    return page

#################
# School years ##
#################
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.years.getList', 'jtStartIndex','jtPageSize', 'jtSorting'])
def jsonp_years_list(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    sorting = request.params['jtSorting'].split(" ")
    print sorting
    query = DBSession.query(SchoolYears).offset(int(start_index)).limit(int(page_size))
    for position in query:
        page['Records'].append({"year_id": position.id,
                                "start": str(position.start),
                                "end": str(position.end),
                                "modification_date": str(position.modification_date).split(" ")[0]
                                })
    page['TotalRecordCount'] = DBSession.query(Schedules).count()
    return page


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.years.delete', 'year_id'])
def jsonp_years_delete(request):
    session = DBSession()
    year = DBSession.query(SchoolYears).filter_by(id=request.params['year_id']).first()
    session.delete(year)
    transaction.commit()
    return {"Result":"OK"}


@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.years.edit', 'year_id', 'start', 'end'])
def jsonp_years_edit(request):
    session = DBSession()
    year = DBSession.query(SchoolYears).filter_by(id=request.params['year_id']).first()
    year.start=datetime.datetime(*(time.strptime(request.params['start'], "%Y-%m-%d")[0:6]))
    year.end=datetime.datetime(*(time.strptime(request.params['end'], "%Y-%m-%d")[0:6]))
    year.modification_date = datetime.datetime.now()
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.years.add', 'start', 'end'])
def jsonp_years_create(request):
    page={"Result":"OK"}
    session = DBSession()
    start=datetime.datetime(*(time.strptime(request.params['start'], "%Y-%m-%d")[0:6]))
    end=datetime.datetime(*(time.strptime(request.params['end'], "%Y-%m-%d")[0:6]))
    schedule = SchoolYears(start,end)
    session.add(schedule)
    session.flush()
    page["Record"]={"year_id": schedule.id,
                    "start": str(schedule.start),
                    "end": str(schedule.end),
                    "modification_date":str(schedule.modification_date).split(" ")[0]
                    }
    transaction.commit()
    return page



#########
# Other #
#########
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp','method=lerni.teachers.getList'])
def api_jsonp_lerni_teachers_getlist(request):
    page={"Result": "OK","Options": []}
    for position in DBSession.query(Teachers):
        page['Options'].append({"DisplayText": position.user.full_name, "Value":position.id})
    return page

@view_config(route_name='options_subjects_list', renderer='jsonp')
def options_subjects_list(request):
    page = {"Result": "OK","Options": []}
    for position in DBSession.query(Subjects):
        page['Options'].append({"DisplayText": position.name, "Value":position.id})
    return page

@view_config(route_name='options_groups_list', renderer='jsonp')
def options_groups_list(request):
    page={"Result": "OK","Options": []}
    for position in DBSession.query(Groups):
        page['Options'].append({"DisplayText":position.name,"Value":position.id})
    return page


############
# Folders ##
############
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp',
            'method=lerni.folders.getList', 'jtStartIndex','jtPageSize', 'jtSorting'])
def jsonp_folders_get_list(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    sorting = request.params['jtSorting'].split(" ")
    page_size = request.params['jtPageSize']
    user = DBSession.query(People).filter_by(email=logged_in).first()
    query = DBSession.query(Folders).filter_by(user=user).filter_by(deleted=False)\
        .offset(int(start_index)).limit(int(page_size))
    for position in query:
        folder_data = DBSession.query(FoldersVersions).filter_by(folder_id=position.id).order_by('-id').first()
        try:
            page['Records'].append({"folder_id":position.id,
                                    "title":folder_data.title,
                                    "tags":folder_data.tags,
                                    "css":folder_data.css_id,
                                    "gpg":position.sign,
                                    "published":str(position.state)
                                    })
        except DBAPIError:
            return {"Result":"ERROR","Message":"Coś jest nie tak :/"}
    page['TotalRecordCount'] = DBSession.query(Folders).filter_by(user=user).filter_by(deleted=False)\
        .offset(int(start_index)).limit(int(page_size)).count()
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.folders.delete',
                                                                'folder_id'])
def jsonp_folders_delete(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    session = DBSession()
    user = DBSession.query(People).filter_by(email=logged_in).first()
    folder = DBSession.query(Folders).filter_by(id=request.params['folder_id']).first()
    if not folder:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    elif folder.user.id == user.id:
        folder.deleted = True
        transaction.commit()
        return {"Result":"OK"}
    else:
        return {"Result":"ERROR","Message":"Ten folder nie należy do Ciebie. Nie możesz go usunąć."}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.folders.edit',
                                                                "folder_id","title","tags","css","gpg","published"])
def jsonp_folders_edit(request):
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    session = DBSession()
    folder = DBSession.query(Folders).filter_by(id=request.params['folder_id']).first()
    if not folder:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    folder_data = FoldersVersions(folder.id, request.params["title"], request.params["tags"],
                                  request.params["css"])
    folder.state={'True':True,'False':False}[request.params["published"]]
    folder.sign=request.params["gpg"]
    session.add(folder_data)
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.folders.add',
                                                                "title","tags","css","gpg","published"])
def jsonp_folders_add(request):
    page={"Result":"OK","Record":[]}
    logged_in = authenticated_userid(request)
    if not logged_in:
        return {"Result":"ERROR","Message":"User not logged in."}
    session = DBSession()
    user = DBSession.query(People).filter_by(email=logged_in).first()
    folder = Folders(user.id)
    if not folder:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    session.add(folder)
    session.flush()
    session.refresh(folder)
    folder_data = FoldersVersions(folder.id, request.params["title"], request.params["tags"],
                                  request.params["css"])
    folder.state={'True':True,'False':False}[request.params["published"]]
    folder.sign = request.params["gpg"]
    session.add(folder_data)
    page['Record'].append({"folder_id": folder_data.id,
                           "title": folder_data.title,
                            "tags": folder_data.tags,
                            "css": folder_data.css_id,
                            "gpg": folder.sign})
    transaction.commit()
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
        return {"Result": "ERROR", "Message": "User not logged in."}
    if {"Title", "Tags", "CSS", "GPG", "Published"} <= set(request.params):
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
    if {"FolderID", "Title", "Tags", "CSS", "Published"} <= set(request.params):
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






###########
# Tweets ##
###########
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.tweets.getList'])
def api_jsonp_lerni_tweets_getlist(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    if 'jtSorting' in request.params:
        sorting = request.params['jtSorting'].split(" ")
    query = DBSession.query(Tweets).offset(int(start_index)).limit(int(page_size))
    for position in query:
        cat = []
        for x in position.categories:
            cat.append(x.category.name)
        page['Records'].append({u"tweet_id": position.id,
                                u"user": position.user_id,
                                u"text": position.text,
                                u"link_name": position.link_name,
                                u"link": position.link,
                                u"state": position.state,
                                u"categories": " ".join(cat),
                                u"modification_date": str(position.modification_date)})
    page['TotalRecordCount'] = DBSession.query(Tweets).count()
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.tweets.delete','user_id'])
def api_jsonp_lerni_tweets_delete(request):
    session = DBSession()
    user = DBSession.query(People).filter_by(id=request.params['user_id']).first()
    if not user:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    elif not user.email_confirmed:
        session.delete(user)
        transaction.commit()
        return {"Result":"OK"}
    else:
        return {"Result": "ERROR", "Message": "Nie można usunąć użytkownika, który potwierdził swój adres email."}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.tweets.edit',
                                                                "user_id", "first_name", "second_name", "last_name",
                                                                "pesel", "birth_date", "email", "password", "group"])
def api_jsonp_lerni_tweets_edit(request):
    session = DBSession()
    user = DBSession.query(People).filter_by(id=request.params['user_id']).first()
    if not user:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    user.first_name = request.params["first_name"]
    user.second_name = request.params["second_name"]
    user.last_name = request.params["last_name"]
    user.pesel = request.params["pesel"]
    user.birth_date = datetime.datetime(*(time.strptime(request.params['birth_date'], "%Y-%m-%d")[0:6]))
    user.phone_number = request.params["phone_number"]
    user.email = request.params["email"]
    if request.params["password"] != "do_not_change":
        user.password = hashlib.sha512(unicode(request.params["password"]+
                                               str(user.registration_date).encode('utf-8'))).hexdigest()
    user.group_id = request.params["group"]
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp','method=lerni.tweets.add',
            "first_name", "second_name", "last_name", "pesel", "birth_date", "email", "password", "group"])
def api_jsonp_lerni_tweets_add(request):
    page={"Result":"OK","Record":[]}
    try:
        session = DBSession()
        wallet = Wallet(0)
        session.add(wallet)
        session.flush()
        session.refresh(wallet)
        user = People(request.params["first_name"], request.params["second_name"], request.params["last_name"],
                      request.params["pesel"],
                      datetime.datetime(*(time.strptime(request.params['birth_date'], "%Y-%m-%d")[0:6])),
                      request.params["phone_number"],request.params["email"],request.params["password"],
                      "","",wallet.id,0,0,0,request.params["group"])
        session.add(user)
        page['Record'].append({"user_id":user.id,"first_name":user.first_name,
                                "second_name":user.second_name,"last_name":user.last_name,
                                "pesel":user.pesel,"birth_date":str(user.birth_date.date()),
                                "email":user.email,"phone_number":user.phone_number,
                                "password":"do_not_change","group":1})
        transaction.commit()
    except DBAPIError:
        return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
    except ValueError:
        return {"Result":"ERROR","Message":"Nieprawidłowa data urodzenia :/"}
    return page


############
# Folders ##
############
@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.folders.getList'])
def api_jsonp_lerni_folders_getlist(request):
    page = {"Result":"OK","Records":[]}
    start_index = request.params['jtStartIndex']
    page_size = request.params['jtPageSize']
    if 'jtSorting' in request.params:
        sorting = request.params['jtSorting'].split(" ")
    query = DBSession.query(Tweets).offset(int(start_index)).limit(int(page_size))
    for position in query:
        cat = []
        for x in position.categories:
            cat.append(x.category.name)
        page['Records'].append({u"tweet_id": position.id,
                                u"user": position.user_id,
                                u"text": position.text,
                                u"link_name": position.link_name,
                                u"link": position.link,
                                u"state": position.state,
                                u"categories": " ".join(cat),
                                u"modification_date": str(position.modification_date)})
    page['TotalRecordCount'] = DBSession.query(Tweets).count()
    return page

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.folders.delete','user_id'])
def api_jsonp_lerni_folders_delete(request):
    session = DBSession()
    user = DBSession.query(People).filter_by(id=request.params['user_id']).first()
    if not user:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    elif not user.email_confirmed:
        session.delete(user)
        transaction.commit()
        return {"Result":"OK"}
    else:
        return {"Result": "ERROR", "Message": "Nie można usunąć użytkownika, który potwierdził swój adres email."}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp', 'method=lerni.folders.edit',
                                                                "user_id", "first_name", "second_name", "last_name",
                                                                "pesel", "birth_date", "email", "password", "group"])
def api_jsonp_lerni_folders_edit(request):
    session = DBSession()
    user = DBSession.query(People).filter_by(id=request.params['user_id']).first()
    if not user:
        return {"Result":"ERROR","Message":"Coś poszło nie tak :/"}
    user.first_name = request.params["first_name"]
    user.second_name = request.params["second_name"]
    user.last_name = request.params["last_name"]
    user.pesel = request.params["pesel"]
    user.birth_date = datetime.datetime(*(time.strptime(request.params['birth_date'], "%Y-%m-%d")[0:6]))
    user.phone_number = request.params["phone_number"]
    user.email = request.params["email"]
    if request.params["password"] != "do_not_change":
        user.password = hashlib.sha512(unicode(request.params["password"]+
                                               str(user.registration_date).encode('utf-8'))).hexdigest()
    user.group_id = request.params["group"]
    transaction.commit()
    return {"Result":"OK"}

@view_config(route_name='api', renderer='jsonp', request_param=['format=jsonp','method=lerni.folders.add',
            "first_name", "second_name", "last_name", "pesel", "birth_date", "email", "password", "group"])
def api_jsonp_lerni_folders_add(request):
    page={"Result":"OK","Record":[]}
    try:
        session = DBSession()
        wallet = Wallet(0)
        session.add(wallet)
        session.flush()
        session.refresh(wallet)
        user = People(request.params["first_name"], request.params["second_name"], request.params["last_name"],
                      request.params["pesel"],
                      datetime.datetime(*(time.strptime(request.params['birth_date'], "%Y-%m-%d")[0:6])),
                      request.params["phone_number"],request.params["email"],request.params["password"],
                      "","",wallet.id,0,0,0,request.params["group"])
        session.add(user)
        page['Record'].append({"user_id":user.id,"first_name":user.first_name,
                                "second_name":user.second_name,"last_name":user.last_name,
                                "pesel":user.pesel,"birth_date":str(user.birth_date.date()),
                                "email":user.email,"phone_number":user.phone_number,
                                "password":"do_not_change","group":1})
        transaction.commit()
    except DBAPIError:
        return {"Result":"ERROR","Message":"Form is not valid! Please correct it and try again."}
    except ValueError:
        return {"Result":"ERROR","Message":"Nieprawidłowa data urodzenia :/"}
    return page
