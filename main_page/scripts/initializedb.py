# -*- coding: utf-8 -*-
import os
import sys
import transaction
import datetime

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
    Articles,
    ArticlesContent,
    ArticlesCategories,
    ArticlesMainPage,
    Articles_Comments,
    Users_Groups,
    Base,
    Substitutions,
    Occupations,
    Titles,
    People,
    Absent,
    Replace,
    Duty,
    Shift,
    Places,
    Subjects,
    Schedules,
    LuckyNumbers,
    SchoolYears,
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
    CompetitorsGroups
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        DBSession.add_all([
        MenuTop(u'Strona Główna', "/"),
        MenuTop(u'Zastępstwa', "/zastepstwa"),
        MenuTop(u'Dla kandydatów', "/p/dla-kandydatow"),
        MenuTop(u'Dla rodziców', "/p/dla-rodzicow"),
        MenuTop(u'Poznaj Staszica', "/p/poznaj-staszica"),
        MenuTop(u'Nasze sukcesy', "/nasze-sukcesy"),
        MenuTop(u'Support!', "/support"),
        MenuTop(u'Czat', "http://czat.staszic.edu.pl/"),
        MenuTop(u'SIS', "http://sis.staszic.edu.pl/")])
    with transaction.manager:
        DBSession.add_all([
        ArticlesCategories("Sukcesy"),
        Articles(datetime.datetime.now(), 1, 1, 1, 1, 0),
        ArticlesMainPage(1,1,2),
        ArticlesContent(1,u"Pierwszy artykuł",u"Oto przykładowy artykuł - usuń go, a następnie zastap czymś sensownym.",datetime.datetime.now(),1),
        ])
    #with transaction.manager:
    #    DBSession.add_all([
    #    Articles_Comments(5,datetime.datetime.now(),1,"WEEE!")
    #    ])
    with transaction.manager:
        DBSession.add_all([
        Users_Groups("group:admin"),
        Users_Groups("group:basic")])
        
    with transaction.manager:
        DBSession.add_all([
        MenuLeft(u'Strona Główna', "/"),
        MenuLeft(u'Historia Szkoły', "/history"),
        MenuLeft(u'Olimpijczycy', "/competitors"),
        MenuLeft(u'Absolwenci', "/graduates"),
        MenuLeft(u'Fundacja', "/foundation"),
        MenuLeft(u'Towarzystwo S. T.', "/companionship"),       #Dodać
        #MenuLeft(u'Statuty i Reg.', "/"),      #--> "Do pobrania"
        MenuLeft(u'Galeria', "/gallery"),
        MenuLeft(u'Kontakt', "/p/kontakt"),
        MenuLeft(u'Dojazd', "/p/dojazd"),
        ##MenuLeft(u'Forum (?))', "/"),
        MenuLeft(u'Plan Lekcji', "http://sis.staszic.edu.pl/schedule"),
        MenuLeft(u'Panorama', "http://samorzad.staszic.edu.pl/panorama"),
        #MenuLeft(u'Kalendarium', "/"),
        #MenuLeft(u'Projekt SZP', "/"),
        MenuLeft(u'Szczęśliwy numerek', "http://sis.staszic.edu.pl/lucky"),
        MenuLeft(u'Podręczniki', "/books"),
        MenuLeft(u'Konkursy', "/competitions")
        
        ]) #<!-- LINK DO FACEBOOKA i BLIPA GDZIEŚ -->
    with transaction.manager:
        DBSession.add_all([
        Substitutions(date_for=datetime.datetime.today(),date_as=datetime.datetime.today(),published=datetime.datetime.now(),suit=True,comments="test")])
    with transaction.manager:
        DBSession.add_all([
        Occupations("uczen"),
        Occupations("nauczyciel"),
        Titles("mgr"),
        Titles("dr"),
        Titles("ks."),
        People(u"Administrator","",u"","pesel","2","1",u"admin",u"Administrator",u"admin","123456789",1),
        AppCodes(63, "some_text", u"some_text", u"some_text"),
        SupportSections(u"Dział IT"),
        SupportSections(u"Sekretariat"),
        SupportSections(u"Księgowość"),
        SupportSubSections(1,u"Dostęp do sieci WI-FI","wifi"),
        SupportSubSections(1,u"Problem z aplikacją mobilną","mobile"),
        SupportSubSections(1,u"Strona internetowa (błedy w tekście)","tekst"),
        SupportSubSections(1,u"Strona internetowa (błędy w wyświetlaniu strony)","design"),
        SupportSubSections(1,u"Strona internetowa (błedy w działaniu)","working"),
        SupportSubSections(2,u"Rekrutacja","recruitment"),
        SupportSubSections(3,u"Składki dla rodziców","kasa"), ##
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
        Duty(2,2,2,2,1),
        Subjects(u"angielski",u"ang"),
        Subjects(u"biologia",u"bio"),
        Subjects(u"chemia",u"chem"),
        Subjects(u"przedsiębiorczość",u"eko"),
        Subjects(u"fizyka",u"fiz"),
        Subjects(u"francuski",u"fr"),
        Subjects(u"geografia",u"geo"),
        Subjects(u"historia",u"hist"),
        Subjects(u"informatyka",u"inf"),
        Subjects(u"labolatorium",u"lab"),
        Subjects(u"matematyka",u"mat"),
        Subjects(u"muzyka",u"muz"),
        Subjects(u"niemiecki",u"niem"),
        Subjects(u"plastyka",u"plast"),
        Subjects(u"prawo",u"prawo"),
        Subjects(u"przysposobienie obronne",u"po"),
        Subjects(u"polski",u"pol"),
        Subjects(u"religia",u"rel"),
        Subjects(u"rosyjski",u"ros"),
        Subjects(u"technika",u"tech"),
        Subjects(u"wychowanie fizyczne",u"wf"),
        Subjects(u"wiedza o kulturze",u"wok"),
        Subjects(u"wiedza o społeczeństwie",u"wos"),
        Subjects(u"ZWO",u"zwo"),
        Subjects(u"edukacja dla bezpieczeństwa",u"edb")])
    with transaction.manager:
        DBSession.add_all([
        Schedules(1,datetime.date(2012, 9, 3),datetime.date(2013, 2, 8),datetime.datetime(2012, 9, 3, 18, 40, 43)),
        LuckyNumbers(datetime.date(2012, 9, 3), 1),
        LuckyNumbers(datetime.date(2012, 9, 4), 2),
        LuckyNumbers(datetime.date(2012, 9, 5), 3),
        LuckyNumbers(datetime.date(2012, 9, 6), 4),
        SchoolYears(datetime.date(2012, 9, 3),datetime.date(2013, 6, 28),datetime.datetime.now()),
        Groups(u"1gm"),
        Groups(u"1bch1"),
        Groups(u"1bch2"),
        Groups(u"1pol"),
        Groups(u"1mat1"),
        Groups(u"1mat2"),
        Groups(u"1a"),
        Groups(u"1b"),
        Groups(u"1c"),
        Groups(u"1d"),
        Groups(u"1e"),
        Groups(u"2gm"),
        Groups(u"2jęz"),
        Groups(u"2bch"),
        Groups(u"2pol"),
        Groups(u"2mat1"),
        Groups(u"2mat2"),        
        Groups(u"2rchem1"),
        Groups(u"2rchem2"),
        Groups(u"2rfiz1"),
        Groups(u"2rfiz2"),
        Groups(u"2rgeo"),
        Groups(u"2rinf"),
        Groups(u"2rpol"),
        Groups(u"2rwos"),
        Groups(u"2a"),
        Groups(u"2b"),
        Groups(u"2c"),
        Groups(u"2d"),
        Groups(u"2e1"),
        Groups(u"2e2"),
        Groups(u"3gm"),
        Groups(u"3jęz"),
        Groups(u"3bch"),
        Groups(u"3pol"),
        Groups(u"3mat1"),
        Groups(u"3mat2"),
        Groups(u"3rchem1"),
        Groups(u"3rchem2"),
        Groups(u"3rfiz"),
        Groups(u"3rgeo"),
        Groups(u"3rinf"),
        Groups(u"3rpol"),
        Groups(u"3rwos"),
        Groups(u"3a"),
        Groups(u"3b"),
        Groups(u"3c"),
        Groups(u"3d"),
        Groups(u"3e")])
        #Lessons(1, teacher_subject_id, group_id, part_1, part_2, day, order, room)
        import_pages()
        import_competitors()
        import_tweets()
        
def import_competitors():
    mypath="../main_page/main_page/data/competitors/"
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
    mypath="../main_page/main_page/data/pages/"
    page_id=0
    for x in [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]:
        f = codecs.open(mypath+x, "r", "utf-8")
        tekst = f.read().split("\n")
        f.close()
        page_id+=1
        with transaction.manager:
            DBSession.add_all([Pages(tekst[0].split("|||")[0], tekst[0].split("|||")[1])])
        data=""
        for y in tekst[1:]:
            if len(y)>0:
                if y[0]=="#":
                    if data!="":
                        with transaction.manager:
                            DBSession.add_all([ SubPages(page_id, url_name, name, data) ])
                    url_name=y.split("|||")[0][1:]
                    name=y.split("|||")[1]
                    data=""
                else:
                    data+=y 
        if data!="":
            with transaction.manager:
                DBSession.add_all([ SubPages(page_id, url_name, name, data) ])
def import_tweets():
    mypath="../main_page/main_page/data/tweets/"
    for x in [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]:
        f = codecs.open(mypath+x, "r", "utf-8")
        tekst = f.read().split("\n")
        f.close()
        with transaction.manager:
            DBSession.add_all([TweetsCategories(x)])
        category_id=1
        data=""
        for y in tekst[1:]:
            if len(y)>0:
                if y[0]=="#":
                    if data!="":
                        with transaction.manager:
                            DBSession.add_all([ DBSession.add_all([Tweets(datetime.datetime.now(), pesel,1,category_id, data) ]) ])
                    date=y.split("|||")[0]
                    pesel=y.split("|||")[1]
                    data=""
                else:
                    data+=y 
        if data!="":
            with transaction.manager:
                DBSession.add_all([ SubPages(page_id, url_name, name, data) ])
                
    
    
    
    for x in [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]:
        f = codecs.open(mypath+x, "r", "utf-8")
        tekst = f.read().split("|||")
        f.close()
        with transaction.manager:
            DBSession.add_all([TweetsCategories(x)])
        for y in tekst:
            if len(y)>0:
                with transaction.manager:
                    DBSession.add_all([Tweets(add_date, author_id,state,category_id, hits, content) ])
