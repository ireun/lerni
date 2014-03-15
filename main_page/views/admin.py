# -*- coding: utf-8 -*-
from base import *


@view_config(route_name='admin_home')
def admin_home(request):
    return HTTPFound(location=request.route_path('admin', page='overview'))


@view_config(route_name='admin', renderer='admin_overview.mak', match_param='page=overview')
def admin_overview(request):
    page = {'allerts': []}
    page.update(get_basic_account_info(request))
    page['rows'] = [[], [], [], [], [], [], [], [], [], []]
    for position in DBSession.query(Pages).filter_by(url_name='overview').first().widgets:
        soup = BeautifulSoup(position.data)
        [s.extract() for s in soup(['script', 'iframe', 'img', 'object', 'embed', 'param'])]
        data = parser.format(unicode(soup), somevar='somevalue')
        page['rows'][position.row].append(["", position.size_x, position.add_class, data])
    return page


@view_config(route_name='admin', renderer='admin_gallery.mak', match_param='page=gallery')
def admin_gallery(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin", u"Panel Administratora"], ["", u"Overview"]], 'allerts': []}
    page.update(get_basic_account_info(request))
    return page


@view_config(route_name='admin', renderer='admin_layout_edit.mak', match_param='page=layouts')
def admin_layouts(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Użytkownicy"]], 'allerts': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Użytkownicy"
    page['title_desc'] = u"Wybierz stonę, której layout chcesz edytować."
    return page


@view_config(route_name='admin', renderer='admin_jtable.mak', match_param='page=users')
def admin_users(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Użytkownicy"]], 'allerts': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Użytkownicy"
    page['title_desc'] = u'''Poniżej możesz dodać nowych albo edyotwać istniejąch użytkowników.
                        Jeśli to możliwe spróbuj jednak zasugerować im aby dokonali zmian samodzielnie.'''
    page['sorting'] = True
    page['defaultSorting'] = "user_id DESC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.users.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.users.delete"
    page['update'] = "/api?format=jsonp&method=lerni.users.edit"
    page['create'] = "/api?format=jsonp&method=lerni.users.add"
    page['fields'] = [{'name': u"user_id", 'key': True, "list": False, "create": False, "edit": False}]
    page['fields'].append({'name': u"first_name", "title": u"Imię"})
    page['fields'].append({'name': u"second_name", "title": u"Drugie Imię"})
    page['fields'].append({'name': u"last_name", "title": u"Nazwisko"})
    page['fields'].append({'name': u"pesel", "title": u"Pesel"})
    page['fields'].append({'name': u"phone_number", "title": u"Numer telefonu"})
    page['fields'].append({'name': u"birth_date", "title": u"Data urodzenia", "type": "date",
                           "displayFormat": "dd.mm.yy"})
    page['fields'].append({'name': u"email", "title": u"Email"})
    page['fields'].append({'name': u"password", "title": u"Hasło"})
    page['fields'].append({'name': u"group", "title": u"Grupa"})
    return page


@view_config(route_name='admin', renderer='admin_people.mak', match_param='page=people')
def admin_people(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", "Nauczyciele"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Nauczyciele"
    page['title_desc'] = u"Tutaj możesz dodać lub usunąć nauczycieli."
    can_teachers = []
    emp_teachers = []
    ex_teachers = []
    for position in DBSession.query(Teachers):
        if position.state==0:
            can_teachers.append([["",position.user.full_name],
                                 ["hidden-phone", "x"],
                                 ["hidden-phone","y"],
                                 ["hidden-phone","z"],
                                 ["","w"]])
        elif position.state==1:
            emp_teachers.append([["",position.user.full_name],
                                 ["hidden-phone", "x"],
                                 ["hidden-phone","y"],
                                 ["hidden-phone","z"],
                                 ["","w"]])
        elif position.state==2:
            ex_teachers.append([["",position.user.full_name],
                                ["hidden-phone", "x"],
                                ["hidden-phone","y"],
                                ["hidden-phone","z"],
                                ["","w"]])
    table_head=[[u"",u"Imię i Nazwisko"],
                [u"hidden-phone",u"Przemiot"],
                [u"hidden-phone",u"Ilość uczonych klas"],
                [u"hidden-phone",u"Wychowawstwo"],
                [u"",u"Akcje"]]
    page['tables'].append(["1", u"Zatrudnieni", table_head, emp_teachers])
    page['tables'].append(["2", u"Oczekujący", table_head, can_teachers])
    page['tables'].append(["3", u"Byli", table_head, ex_teachers])
    return page

@view_config(route_name='admin', renderer='admin_people.mak', match_param='page=personel')
def admin_personel(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["","Personel"]], 'allerts': [], 'tables': []}
    page.update(get_basic_account_info(request))
    page['title']=u"Personel"
    page['title_desc']=u"Tutaj możesz dodać lub usunąć personel."
    can_teachers=[] #candidate
    emp_teachers=[] #employed
    ex_teachers=[]
    for position in DBSession.query(Teachers):
        if position.state==0: can_teachers.append([["",position.user.full_name],["hidden-phone", "x"],["hidden-phone","y"],["hidden-phone","z"],["","w"]])
        elif position.state==1: emp_teachers.append([["",position.user.full_name],["hidden-phone", "x"],["hidden-phone","y"],["hidden-phone","z"],["","w"]])
        elif position.state==2: ex_teachers.append([["",position.user.full_name],["hidden-phone", "x"],["hidden-phone","y"],["hidden-phone","z"],["","w"]])
    table_head=[[u"",u"Imię i Nazwisko"],[u"hidden-phone",u"Przemiot"],[u"hidden-phone",u"Ilość uczonych klas"],[u"hidden-phone",u"Wychowawstwo"],[u"",u"Akcje"]]
    page['tables'].append(["1",u"Zatrudnieni",table_head, emp_teachers])
    page['tables'].append(["2",u"Oczekujący",table_head, can_teachers])
    page['tables'].append(["3",u"Byli",table_head, ex_teachers])
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=log', 'page=years'])
def admin_log_years(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["","Lata szkolne"]], 'allerts':[], 'tables':[]}
    page.update(get_basic_account_info(request))
    page['title'] = u"Lata szkolne"
    page['title_desc'] = u"Aby dodać nowy rok szkolny skorzystaj z formularza poniżej."
    page['sorting'] = True
    page['defaultSorting'] = "start DESC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.years.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.years.delete"
    page['update'] = "/api?format=jsonp&method=lerni.years.edit"
    page['create'] = "/api?format=jsonp&method=lerni.years.add"
    page['fields'] = [{'name': "year_id", 'key': True, "list": False, "create": "true", "edit": False}]
    page['fields'].append({'name': "start", "title": u"Początek roku szkolnego", "type": "date",
                           "displayFormat": "dd.mm.yy"})
    page['fields'].append({'name': "end", "title": u"Koniec roku szkolnego", "type": "date",
                           "displayFormat": "dd.mm.yy"})
    page['fields'].append({'name': "modification_date", "title": "Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": False, "edit": False, "sorting": False})
    return page


@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=log', 'page=subjects'])
def admin_log_subjects(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", "Przedmioty"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Przedmioty"
    page['title_desc'] = u"Utwórz listę przedmiotów nauczanych w twojej szkole."
    page['sorting'] = True
    page['defaultSorting'] = "name ASC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.subjects.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.subjects.delete"
    page['update'] = "/api?format=jsonp&method=lerni.subjects.edit"
    page['create'] = "/api?format=jsonp&method=lerni.subjects.add"
    page['fields'] = [{'name': "subject_id", 'key': True, "list": False, "create": "true", "edit": False}]
    page['fields'].append({'name': "name", "title": u"Pełna nazwa"})
    page['fields'].append({'name': "short", "title": u"Skrócona nazwa"})
    page['fields'].append({'name': "modification_date", "title": "Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": False, "edit": False, "sorting": False})
    return page


@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=all', 'page=tweets'])
def admin_log_tweets(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", "Przedmioty"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Wszystkie Tweety"
    page['title_desc'] = u"Oto lista wszystkich tweetów w bazie danych twojej szkoły."
    page['sorting'] = True
    page['defaultSorting'] = "name ASC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.tweets.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.tweets.delete"
    page['update'] = "/api?format=jsonp&method=lerni.tweets.edit"
    page['create'] = "/api?format=jsonp&method=lerni.tweets.add"
    page['fields'] = [{'name': "tweet_id", 'key': True, "list": False, "create": "true", "edit": False}]
    page['fields'].append({'name': "user", "title": u"Autor"})
    page['fields'].append({'name': "text", "title": u"Text"})
    page['fields'].append({'name': "link_name", "title": u"Text Linku"})
    page['fields'].append({'name': "link", "title": u"Link"})
    page['fields'].append({'name': "categories", "title": u"Kategorie"})
    page['fields'].append({'name': "state", "title": u"Stan"})
    page['fields'].append({'name': "modification_date", "title": "Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": False, "edit": False, "sorting": False})
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=all', 'page=graduates'])
def admin_log_graduates(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Absolwenci"]], 'allerts': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Absolwenci"
    page['title_desc'] = u'''Poniżej możesz edytować listę absolwentów.'''
    page['sorting'] = True
    page['defaultSorting'] = "id DESC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.graduates.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.graduatess.delete"
    page['update'] = "/api?format=jsonp&method=lerni.graduates.edit"
    page['create'] = "/api?format=jsonp&method=lerni.graduates.add"
    page['fields'] = [{'name': u"id", 'key': True, "list": False, "create": False, "edit": False}]
    page['fields'].append({'name': u"name", "title": u"Imię i nazwisko"})
    page['fields'].append({'name': u"graduation", "title": u"Matura"})
    page['fields'].append({'name': u"about", "title": u"O absolwencie"})
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=all', 'page=competitors'])
def admin_log_competitors(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Użytkownicy"]], 'allerts': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Konkursowicze"
    page['title_desc'] = u'''Poniżej możesz dodać nowych albo edyotwać istniejąch konkursowiczów.'''
    page['sorting'] = True
    page['defaultSorting'] = "competitor_id DESC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.competitors.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.competitors.delete"
    page['update'] = "/api?format=jsonp&method=lerni.competitors.edit"
    page['create'] = "/api?format=jsonp&method=lerni.competitors.add"
    page['fields'] = [{'name': u"competitor_id", 'key': True, "list": False, "create": False, "edit": False}]
    page['fields'].append({'name': u"first_name", "title": u"Imię"})
    page['fields'].append({'name': u"last_name", "title": u"Nazwisko"})

    page['fields'].append({'name': u"competition_group_id", "title": u"Poziom", "options": "/api?format=jsonp&method=lerni.competitors.groups.nameList"})
    page['fields'].append({'name': u"competition_id", "title": u"Konkurs", "options": "/api?format=jsonp&method=lerni.competitors.competitions.nameList"})
    page['fields'].append({'name': u"competitor_type_id", "title": u"Osiągnięcie", "options": "/api?format=jsonp&method=lerni.competitors.types.nameList"})
    page['fields'].append({'name': u"competitor_tutor_id", "title": u"Opiekun",
                           "options": "/api?format=jsonp&method=lerni.competitors.tutors.nameList"})
    page['fields'].append({'name': u"year", "title": u"Rok szkolny"})
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=all', 'page=competitions'])
def admin_log_competitions(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Użytkownicy"]], 'allerts': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Konkursy"
    page['title_desc'] = u'''Poniżej możesz dodać i usuwać konkursy.'''
    page['sorting'] = True
    page['defaultSorting'] = "competition_id DESC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.competitions.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.competitions.delete"
    page['update'] = "/api?format=jsonp&method=lerni.competitions.edit"
    page['create'] = "/api?format=jsonp&method=lerni.competitions.add"
    page['fields'] = [{'name': u"competition_id", 'key': True, "list": False, "create": False, "edit": False}]
    page['fields'].append({'name': u"name", "title": u"Nazwa"})
    page['fields'].append({'name': u"subject_id", "title": u"Przedmiot", "options": "/api?format=jsonp&method=lerni.subjects.nameList"})
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=all', 'page=folders'])
def admin_log_folders(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Przedmioty"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Wszystkie Foldery"
    page['title_desc'] = u"Oto lista wszystkich folderów w bazie danych twojej szkoły."
    page['sorting'] = True
    page['defaultSorting'] = "name ASC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.folders.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.folders.delete"
    page['update'] = "/api?format=jsonp&method=lerni.folders.edit"
    page['create'] = "/api?format=jsonp&method=lerni.folders.add"
    page['fields'] = [{'name': "tweet_id", 'key': True, "list": False, "create": "true", "edit": False}]
    page['fields'].append({'name': "user", "title": u"Autor"})
    page['fields'].append({'name': "text", "title": u"Text"})
    page['fields'].append({'name': "link_name", "title": u"Text Linku"})
    page['fields'].append({'name': "link", "title": u"Link"})
    page['fields'].append({'name': "categories", "title": u"Kategorie"})
    page['fields'].append({'name': "state", "title": u"Stan"})
    page['fields'].append({'name': "modification_date", "title": "Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": False, "edit": False, "sorting": False})
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=log', 'page=lucky'])
def admin_log_lucky(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", u"Szczęśliwe numerki"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Szczęśliwe numerki"
    page['title_desc'] = u"W poniższej tabeli znajdują się szczęśliwe numerki na poszczególne tygodnie."
    page['defaultSorting'] = "name ASC"
    page['list'] = "/api?format=jsonp&method=lerni.lucky.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.lucky.delete"
    page['update'] = "/api?format=jsonp&method=lerni.lucky.edit"
    page['create'] = "/api?format=jsonp&method=lerni.lucky.add"
    page['fields'] = [{'name': "first_date", "title": "From", 'key': True, "list": False, "type": "date",
                       "displayFormat": "dd.mm.yy", "create": "true", "edit": "false", }]
    page['fields'].append({'name': "0", "title": "Pon"})
    page['fields'].append({'name': "1", "title": "Wt"})
    page['fields'].append({'name': "2", "title": u"Śr"})
    page['fields'].append({'name': "3", "title": "Czw"})
    page['fields'].append({'name': "4", "title": "Pt"})
    page['fields'].append({'name': "5", "title": "Sob"})
    page['fields'].append({'name': "6", "title": "Ndz"})
    page['fields'].append({'name': "start", "title": "start", "type": "date", "displayFormat": "dd.mm.yy",
                           "create": "false", "edit": "false", "sorting": "false"})
    page['fields'].append({'name': "end", "title": "end", "type": "date", "displayFormat": "dd.mm.yy",
                           "create": "false", "edit": "false", "sorting": "false"})
    return page


@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=log', 'page=divisions'])
def admin_log_divisions(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", "Kategorie klas"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Kategorie klas"
    page['title_desc'] = u"Utwórz listę kategorii klas w twojej szkole."
    page['sorting'] = True
    page['defaultSorting'] = "name ASC"
    page['list'] = "/api?format=jsonp&method=lerni.divisions.categories.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.divisions.categories.delete"
    page['update'] = "/api?format=jsonp&method=lerni.divisions.categories.edit"
    page['create'] = "/api?format=jsonp&method=lerni.divisions.categories.add"
    page['fields'] = [{'name': 'subject_id', 'key': True, "create": False, "edit": False, "list": False}]
    page['fields'].append({'name': u"name", "title": u"Pełna nazwa"})
    page['fields'].append({'name': u"short", "title": u"Skrócona nazwa"})
    page['fields'].append({'name': u"modification_date", "title": u"Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": "false", "edit": "false", "sorting": "false"})
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=log', 'page=rooms'])
def admin_log_divisions(request):
    page = {'editor': 0, 'breadcrumbs': [["/admin/overview", u"Dashboard"], ["", "Kategorie klas"]], 'allerts': [],
            'tables': []}
    page.update(get_basic_account_info(request))
    page['title'] = u"Sale lekcyjne"
    page['title_desc'] = u"Utwórz listę sal lekcyjnych w twojej szkole. (opcjonalne)"
    page['sorting'] = True
    page['defaultSorting'] = "name ASC"
    page['list'] = "/api?format=jsonp&method=lerni.rooms.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.rooms.delete"
    page['update'] = "/api?format=jsonp&method=lerni.rooms.edit"
    page['create'] = "/api?format=jsonp&method=lerni.rooms.add"
    page['fields'] = [{'name': 'subject_id', 'key': True, "create": False, "edit": False, "list": False}]
    page['fields'].append({'name': u"name", "title": u"Pełna nazwa"})
    page['fields'].append({'name': u"short", "title": u"Skrócona nazwa"})
    page['fields'].append({'name': u"modification_date", "title": u"Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": "false", "edit": "false", "sorting": "false"})
    return page

@view_config(route_name='admin_log_years_groups', renderer='admin_log_groups.mak')
def admin_log_groups(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["","Lata szkolne"],["","2012"]], 'allerts':[], 'tables':[]}
    page.update(get_basic_account_info(request))
    page['title']=u"Lata szkolne"
    page['title_desc']=u"Aby dodać nowy rok szkolny skorzystaj z formularza poniżej."
    page['categories']=[]
    for position in DBSession.query(DivisionsCategories):
        page['categories'].append([position.name,position.short])
    page['groups']=[]
    for position in DBSession.query(Divisions):
        page['groups'].append(['', position.category.short,position.name])
    return page

@view_config(route_name='admin_log_years_groups_students', renderer='admin_log_groups.mak')
def admin_log_groups_students(request):
    page={'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["","Lata szkolne"],["","2012"]], 'allerts':[], 'tables':[]}
    page.update(get_basic_account_info(request))
    page['title']=u"Lata szkolne"
    page['title_desc']=u"Aby dodać nowy rok szkolny skorzystaj z formularza poniżej."
    page['categories']=[]
    for position in DBSession.query(DivisionsCategories):
        page['categories'].append([position.name,position.short])
    page['students_class']=[['','','Kamil Danak']]
    page['students_all']=[['','','Kamil Danak']]
    #for position in DBSession.query(Divisions):	page['students_class'].append(['',position.category.short,position.name])
    #for position in DBSession.query(Divisions):	page['students_all'].append(['',position.category.short,position.name])
    return page

@view_config(route_name='admin_pp', renderer='admin_jtable.mak', match_param=['pp=log', 'page=timetables'])
def admin_log_timetables(request):
    page = {'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["","Lata szkolne"]], 'allerts':[], 'tables':[]}
    page.update(get_basic_account_info(request))
    page['title'] = u"Plan lekcji"
    page['title_desc'] = u"Poniżej możesz dodać nowy albo edyować instniejący plan lekcji."
    page['jtitle'] = u"Plany lekcji"
    page['sorting'] = True
    page['defaultSorting'] = "start DESC"
    page['selecting'] = True
    page['list'] = "/api?format=jsonp&method=lerni.timetables.getList"
    page['delete'] = "/api?format=jsonp&method=lerni.timetables.delete"
    page['update'] = "/api?format=jsonp&method=lerni.timetables.edit"
    page['create'] = "/api?format=jsonp&method=lerni.timetables.add"
    page['fields'] = [{'name': "timetable_id", 'key': True, "list": False, "create": False, "edit": False}]
    page['fields'].append({'name': "start", "title": "start", "type": "date", "displayFormat": "dd.mm.yy",
                           "create": "false", "edit": "false", "sorting": "false"})
    page['fields'].append({'name': "end", "title": "end", "type": "date", "displayFormat": "dd.mm.yy",
                           "create": "false", "edit": "false", "sorting": "false"})
    page['fields'].append({'name': "modification_date", "title": "Data Modyfikacji", "type": "date",
                           "displayFormat": "dd.mm.yy", "create": "false", "edit": "false", "sorting": "false"})
    return page


@view_config(route_name='admin_log_timetables_edit', renderer='admin_log_timetables_edit.mak')
def admin_log_timetables_edit(request):
    page = {'editor':0, 'breadcrumbs':[["/admin/overview",u"Dashboard"],["","Lata szkolne"]], 'allerts':[], 'tables':[]}
    page.update(get_basic_account_info(request))
    page['title'] = u"Plan lekcji"
    page['title_desc'] = u"Nie zapomnij zapisać zmian po skończeniu pracy."
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


    return {'menu_top_list':menu_top_list,
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