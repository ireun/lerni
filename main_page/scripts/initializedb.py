# -*- coding: utf-8 -*-
import os
import sys
import transaction
import datetime
import yaml

import csv #####################################
from sqlalchemy import Table ###################
from sqlalchemy import engine_from_config

from os import listdir
from os.path import isfile, join
import codecs

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    MenuTop,
    MenuLeft,
    Base,
    Substitutions,
    People,
    AALogin,
    Wallet,    
    
    Folders,
    FoldersVersions,
    FoldersCSS,
    FoldersCSSVersions,
    FoldersTags,
    Entries,
    EntriesVersions,
    EntriesCSS,
    EntriesCSSVersions,
    EntriesLikes,
    EntriesTags,
    Tags,

    Tweets,
    TweetsMain,
    TweetsCategories,
    Videos,
    VideosMain,
    Banners,
    Sets,
    SetsItems,
    EasyLinks,
    
    Teachers,
    Absent,
    Replace,
    Duty,
    Shift,
    Places,
    Subjects,
    Schedules,
    LuckyNumbers,
    SchoolYears,
    Terms,
    DivisionsCategories,
    Divisions,
    Groups,
    Lessons,
    LessonsGroups,
    Association,
    AppCodes,
    SupportSections,
    SupportSubSections,
    SupportTickets,
    SupportQuestions,
    Pages,
    Widgets,
    Competitors,
    CompetitorsCompetitions,
    CompetitorsTutors,
    CompetitorsTypes,
    CompetitorsGroups,
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    """

    :param argv:
    """
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    import_users()
    import_sets()
    import_folders()
    import_tweets()
    import_easy_links()
    import_banners()
    date_now=datetime.datetime.today()
    with transaction.manager:
        DBSession.add_all([
        Videos(2, 2, "68137365"),
        VideosMain(1),
        AppCodes(63, "some_text", u"some_text", u"some_text"),
        Association(63,16,1,0),
        Association(63,29,0,1),
        Association(63,20,1,0),
        Absent(8, "", True, True, True, True, True, True, True, True, 1),
        Absent(56, "", True, True, True, True, True, True, True, True, 1),
        Absent(20, "", True, True, True, True, True, True, True, True, 1),
        Absent(6, "", True, True, True, True, True, True, True, True, 1),
        Replace(56, 2, 2, 1, 0, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1),
        Replace(20, 2, 2, 1, 0, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1),
        Shift(u"pierwsza zmiana"),
        Shift(u"druga zmiana"),
        Places(u"minus pierwsze piętro"),
        Places(u"parter"),
        Places(u"pierwsze piętro"),
        Places(u"drugie piętro"),
        Duty(1,1,1,1,1),
        Duty(2,2,2,2,1)])
    import_subjects()
    with transaction.manager:
        import_competitors()
        DBSession.add_all([
        SchoolYears(datetime.date(2013, 9, 3),datetime.date(2014, 6, 28)),
        Terms(1,datetime.date(2013,9,3),datetime.date(2014,2,1)),
        Terms(1,datetime.date(2014,2,2),datetime.date(2014,6,28)),
        Schedules(datetime.date(2013,9,3),datetime.date(2014,2,1))])
        #Lessons(1, teacher_subject_id, group_id, part_1, part_2, day, order, room)
        import_pages()
        import_competitors()
        import_support()
        import_lucky_numbers()
        import_schedules()

def import_competitors():
    mypath="main_page/data/competitors/"
    for x in [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]:
        f = codecs.open(mypath+x, "r", "utf-8")
        tekst = f.read().split("\n")
        f.close()
        for y in tekst:
            if len(y)>0:
                line=y.split("|||")
                if DBSession.query(CompetitorsGroups).filter_by(name=x).first() is None:
                    DBSession.add_all([ CompetitorsGroups(x) ])
                if DBSession.query(CompetitorsCompetitions).filter_by(name=line[1]).first() is None:
                    DBSession.add_all([ CompetitorsCompetitions(line[1]) ])
                if DBSession.query(CompetitorsTypes).filter_by(name=line[2]).first() is None:
                    DBSession.add_all([ CompetitorsTypes(line[2]) ])
                if DBSession.query(CompetitorsTutors).filter_by(name=line[3]).first() is None:
                    DBSession.add_all([ CompetitorsTutors(line[3]) ])
                DBSession.add_all([ Competitors(line[0].split(" ")[0], line[0].split(" ")[1],
                DBSession.query(CompetitorsCompetitions).filter_by(name=line[1]).first().id,
                DBSession.query(CompetitorsTypes).filter_by(name=line[2]).first().id,
                DBSession.query(CompetitorsTutors).filter_by(name=line[3]).first().id,
                line[4].split("/")[0], line[4].split("/")[1], DBSession.query(CompetitorsGroups).filter_by(name=x).first().id) ])

def import_pages():
    f = open('main_page/data/pages.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    for x in dataMap['pages']:
        session = DBSession()
        page = Pages(x['url_name'],x['name'])
        session.add(page)
        transaction.commit()
        for y in x['widgets']:
            session = DBSession()
            widget = Widgets(w, y['column'],y['row'],y['size_x'],y['size_y'],y['data'])
            session.add(widget)
            transaction.commit()
        w+=1

def import_schedules():
    f = open('main_page/data/schedule.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    timetable_id=0
    for x in dataMap['timetables']:
        session = DBSession()
        timetable_id += 1
        schedule=Schedules(datetime.datetime.strptime(x['start'], '%d-%m-%Y').date(),
                                     datetime.datetime.strptime(x['end'], '%d-%m-%Y').date())
        session.add(schedule)
        transaction.commit()
        for y in x['lessons']:
            session = DBSession()
            t = y['teacher']
            s = y['subject']
            teacher = None
            subject=None
            if t != None:
                teacher = DBSession.query(People).filter_by(first_name=t.split(" ")[0],last_name=t.split(" ")[1])
            if teacher != None and teacher.first() != None:
                teacher = DBSession.query(Teachers).filter_by(user_id=teacher.first().id).first()
            else:
                teacher = None
            #if teacher != None:
            #    teacher = teacher[0]
            if s != None:
                subject = DBSession.query(Subjects).filter_by(name=s).first()
            if subject == None:
                subject = Subjects(s,"")
                session.add(subject)
                session.flush()

            if teacher != None:
                lesson = Lessons(timetable_id, teacher.id, subject.id, y['day'], y['order'], y['room'])
                session.add(lesson)
                for g in y['groups']:
                    group = DBSession.query(Groups).filter_by(name=g['name'])
                    group = group.first()
                    if group == None:
                        division = DBSession.query(Divisions).filter_by(name=g['name'][:-1]).first()
                        if division == None:
                            division = Divisions(1,g['name'][:-1],1)
                            session.add(division)
                            session.flush()
                        group = Groups(division.id, g['name'])
                        session.add(group)
                        session.flush()
                    lesson_group=LessonsGroups(lesson.id,group.id)
                    session.add(lesson_group)
                    session.flush()
            transaction.commit()
def import_groups():
    f = open('main_page/data/groups.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    with transaction.manager:
        DBSession.add_all([
            DivisionsCategories(u"Gimnazjum",u"gm"),
            DivisionsCategories(u"Liceum",u"lic"),
            DivisionsCategories(u"Klasy Językowe",u"lk")])
        for x in dataMap['groups']:
            DBSession.add_all([ Divisions(x['category_id'], x['name'], x['year_id']) ])
            DBSession.add_all([Groups(w,x['name']+u"1"),Groups(w,x['name']+u"2")])
            w+=1

def import_support():
    f = open('main_page/data/support.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    with transaction.manager:
        for x in dataMap['sections']:
            DBSession.add_all([SupportSections(x['name'])])
            for y in x['sections']:
                DBSession.add_all([SupportSubSections(w,y['name'],y['short'])])
            w+=1
def import_easy_links():
    f = open('main_page/data/easy_links.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    with transaction.manager:
        for x in dataMap['easy_links']:
            DBSession.add_all([ EasyLinks(x['user_id'], x['name'], x['path']) ])

def import_banners():
    f = open('main_page/data/banners.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    with transaction.manager:
        for x in dataMap['banners']:
            DBSession.add_all([ Banners(x['user_id'],
                                       datetime.datetime.strptime(x['start_date'], '%d/%m/%Y').date(),
                                       datetime.datetime.strptime(x['end_date'], '%d/%m/%Y').date(),
                                       x['link'], x['alternative']) ])

def import_tweets():
    f = open('main_page/data/tweets.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    categories=[]
    with transaction.manager:
        for x in dataMap['tweets']:
            session = DBSession()
            if not x['category'] in categories:
                tweet_category = TweetsCategories(x['category'])
                session.add(tweet_category)
                session.flush()
                categories.append(x['category'])
            else:
                tweet_category = DBSession.query(TweetsCategories).filter_by(name=x['category']).first()
            tweet = Tweets(x['user_id'], x['text'], x['link'], x['link_name'])
            session.add(tweet)
            if x['main']:
                tweet_main = TweetsMain(w,tweet_category.id)
                session.add(tweet_main)
            transaction.commit()
            w+=1


def import_lucky_numbers():
    f = open('main_page/data/lucky.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    with transaction.manager:
        for x in dataMap['numbers']:
            DBSession.add_all([ LuckyNumbers(x['date'], x['number']) ])

def import_folders():
    mypath="./main_page/data/folders/"
    w=1
    z=1
    for x in [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]:
        f = open(mypath+x)
        dataMap = yaml.safe_load(f)
        f.close()
        with transaction.manager:
            DBSession.add_all([ Folders(2), FoldersVersions(w, dataMap['title'], dataMap['tags']) ])
            for x in dataMap['entries']:
                DBSession.add_all([ Entries(2,w), EntriesVersions(z, x['title'], x['text'], x['tags']) ])
                z+=1
            w+=1
def import_subjects():
    f = open('main_page/data/subjects.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    with transaction.manager:
        for x in dataMap['subjects']:
            DBSession.add_all([ Subjects(x['name'], x['short']) ])

def import_sets():
    f = open('main_page/data/sets.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    with transaction.manager:
        for x in dataMap['sets']:
            DBSession.add_all([ Sets(2,x['name']) ])
            for y in x['items']:
                DBSession.add_all([ SetsItems(2,w,y['name'], None, y['link']), ])
            w+=1

def import_users():
    f = open('main_page/data/people/users.yaml')
    dataMap = yaml.safe_load(f)
    f.close()
    w=1
    date_now=datetime.datetime.today()
    with transaction.manager:
        for x in dataMap['users']:
            DBSession.add_all([
                Wallet(0),
                People(x['first_name'],x['second_name'],x['last_name'],x['pesel'],date_now,
                       x['phonenumber'],x['email'],x['password'],x['key_data'],x['fingerprint'],w,
                       x['email_confirmed'],x['gpg_confirmed'],x['phone_confirmed'],x['group_id'])
            ])
            if x['teacher']:
                DBSession.add_all([ Teachers(w)])
            w+=1