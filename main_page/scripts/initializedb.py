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
    Association,
    AppCodes,
    SupportSections,
    SupportSubSections,
    SupportTickets,
    SupportQuestions,
    Pages,
    SubPages,
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
        Teachers(3,1),
        Teachers(4,1),
        Teachers(5,1),
        Teachers(6,0),
        Teachers(7,0),
        Teachers(8,2),

        TweetsMain(1,1),TweetsMain(2,1),TweetsMain(3,1),TweetsMain(4,2),TweetsMain(5,2),TweetsMain(6,2),
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
        DBSession.add_all([
        SchoolYears(datetime.date(2013, 9, 3),datetime.date(2014, 6, 28)),
        Terms(1,datetime.date(2013,9,3),datetime.date(2014,2,1)),
        Terms(1,datetime.date(2014,2,2),datetime.date(2014,6,28)),
        Schedules(datetime.date(2013,9,3),datetime.date(2014,2,1)),

        DivisionsCategories(u"Gimnazjum",u"gm"),
        DivisionsCategories(u"Liceum",u"lic"),
        DivisionsCategories(u"Klasy językowe",u"ling"),
        DivisionsCategories(u"Rozszerzenia",u"roz"),
        Divisions(1,u"1gm",1),
        Divisions(2,u"1bch1",1),
        Divisions(2,u"1bch2",1),
        Divisions(2,u"1pol",1),
        Divisions(2,u"1mat1",1),
        Divisions(2,u"1mat2",1),
        Divisions(3,u"1a",1),
        Divisions(3,u"1b",1),
        Divisions(3,u"1c",1),
        Divisions(3,u"1d",1),
        Divisions(3,u"1e",1),
        Divisions(1,u"2gm",1),
        Divisions(2,u"2jęz",1),
        Divisions(2,u"2bch",1),
        Divisions(2,u"2pol",1),
        Divisions(2,u"2mat1",1),
        Divisions(2,u"2mat2",1),        
        Divisions(4,u"2rchem1",1),
        Divisions(4,u"2rchem2",1),
        Divisions(4,u"2rfiz1",1),
        Divisions(4,u"2rfiz2",1),
        Divisions(4,u"2rgeo",1),
        Divisions(4,u"2rinf",1),
        Divisions(4,u"2rpol",1),
        Divisions(4,u"2rwos",1),
        Divisions(3,u"2a",1),
        Divisions(3,u"2b",1),
        Divisions(3,u"2c",1),
        Divisions(3,u"2d",1),
        Divisions(3,u"2e1",1),
        Divisions(3,u"2e2",1),
        Divisions(1,u"3gm",1),
        Divisions(2,u"3jęz",1),
        Divisions(2,u"3bch",1),
        Divisions(2,u"3pol",1),
        Divisions(2,u"3mat1",1),
        Divisions(2,u"3mat2",1),
        Divisions(4,u"3rchem1",1),
        Divisions(4,u"3rchem2",1),
        Divisions(4,u"3rfiz",1),
        Divisions(4,u"3rgeo",1),
        Divisions(4,u"3rinf",1),
        Divisions(4,u"3rpol",1),
        Divisions(4,u"3rwos",1),
        Divisions(3,u"3a",1),
        Divisions(3,u"3b",1),
        Divisions(3,u"3c",1),
        Divisions(3,u"3d",1),
        Divisions(3,u"3e",1)])
        #Lessons(1, teacher_subject_id, group_id, part_1, part_2, day, order, room)
        #import_pages()
        import_competitors()
        import_support()
        import_lucky_numbers()
def import_support():
    pass
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
    with transaction.manager:
        for x in dataMap['tweets']:
            DBSession.add_all([ Tweets(x['user_id'], x['text'], x['link'], x['link_name']) ])

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
            w+=1
        
def import_competitors():
    mypath="./main_page/data/competitors/"
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