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

    #with transaction.manager:
    #    DBSession.add_all([
    #    Articles_Comments(5,datetime.datetime.now(),1,"WEEE!")
    #    ])
        
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
        
    date_now=datetime.datetime.today()
    with transaction.manager:
        DBSession.add_all([
        Wallet(0),Wallet(0),Wallet(0),Wallet(0),Wallet(0),Wallet(0),Wallet(0),Wallet(0),
        People(u"Administrator",u"",u"","01010100000",date_now,"",u"admin",u"admin","","",1,0,0,0,7),
        People(u"Kamil",u"Mateusz",u"Danak","518158009",date_now,"518158009",u"kamilx3@gmail.com",u"123456789","","",8,1,0,0,1),
        People(u"Jeronim",u"Ignacy",u"Nowak","53111011133",date_now,"",u"JeronimNowak@mail.com",u"Eipoh7ai","","",2,0,0,0,1), #http://www.fakenamegenerator.com/gen-random-pl-pl.php
        People(u"Marek",u"",u"Czerwiec","91042932486",date_now,"",u"JarosławaAdamska@mail.com",u"Eipoh7ai","","",4,0,0,0,1),
        People(u"Judyta",u"",u"Wieczorek","57042877925",date_now,"",u"JudytaWieczorek@mail.com",u"oo6eis1Ahs2","","",3,0,0,0,1), #April 28, 1957
        People(u"Beata",u"Agata","Wysocka", "64122236141",date_now,"",u"BeataWysocka@mail.com",u"axfasd","","",5,0,0,0,1),
        People(u"Krystyn",u"Marian",u"Rutkowski","89092311731",date_now,"",u"KrystynWysocki@mail.com",u"aiHahTeeg4i","","",6,0,0,0,1),
        People(u"Eligia",u"Agata",u"Borkowska","76093062360",date_now,"",u"EligiaBorkowska@mail.com",u"Edewi","","",7,0,0,0,1),
        Folders(2),
        FoldersVersions(1,u"Bezpieczeństwo w sieci",u"security",1),
        FoldersCSS(2),
        FoldersCSSVersions(1,u"sant",u"Styl Świąteczny","body{};"),
        Tags(u"security"), FoldersTags(1,1), ##Powinno się zrobić automatycznie
        Entries(2,1),
        EntriesVersions(1,u"Szyfrowanie emaili za pomocą GPG",u"<p>Granie w Minecrafta z czasem zaczyna się nudzić. Mamy wtedy dwie możliwości - zagrać w coś innego albo urozmaicić grę modami.  Istnieje wiele gotowych paczek modów (Tekkit), które rzadko w 100% odzwierciedlają nasze potrzeby. Poniżej postaram się opisać jak samemu złożyć taką paczkę modów dla Minecrafta 1.6.2.</p>\
		  [diagram]Krowa --> Kurczak: Witaj![/diagram]","security gpg",0),
        Tags(u"gpg"), EntriesTags(1,1), EntriesTags(1,2), ##Powinno się zrobić automatycznie
        EntriesCSS(2),
        EntriesCSSVersions(1,u"sant",u"Styl Świąteczny","body{};"),
        Folders(4),
        FoldersVersions(2,u"Ogłoszenia Szkolne",u"news"),
        Entries(4,2),
        EntriesVersions(2,u'„Wyprawka szkolna” i stypendium szkolne',u'''
Informujemy, że osoby uprawnione do otrzymania dofinansowania do podręczników szkolnych (II klasa LO), mogą składać wnioski do dyrekcji szkoły najpóźniej do 04. 09. 2013 roku.

Wymagane dokumenty:

wniosek o przyznanie dofinansowania;
zaświadczenie / oświadczenie o dochodach;
faktury za książki lub oświadczenie o kwocie wydanej na zakup podręczników.
Więcej informacji i szczegółowy wykaz wymaganych dokumentów na stronie internetowej miasta: http://www.sosnowiec.pl

Tam również znajdują się informacje na temat stypendium szkolnego (wnioski jak co roku składane do 15. 09. w Urzędzie Miasta).
Informacji udzielają również pedagog i psycholog szkolny, pok. 135.''','news'),


        Banners(8, datetime.datetime.today(), datetime.date(2014, 9, 3), "/static/uploads/staszic_header.png", "Logo Staszica"),
        Banners(8, datetime.datetime.today(), datetime.date(2014, 9, 3), "/static/uploads/new_year.png", "Nowy rok szkolny"),
        Teachers(3,1),
        Teachers(4,1),
        Teachers(5,1),
        Teachers(6,0),
        Teachers(7,0),
        Teachers(8,2),
        Tweets(4, u"Znamy już wstępne wyniki tegorocznego egzaminu maturalnego z przedmiotów obowiązkowych. Ze wszystkich egzaminów uczniowie naszego liceum osiągnęli najlepsze wyniki w mieście i zdecydowanie wyższe wyniki niż średnia.", "", ""),
        Tweets(4, u"Rozpoczęcie roku szkolnego 2013/14 odbędzie się o godzinie 9.00. Msza św. w kościele św. Tomasza o 8.00. Zbiórka I klasy gimnazjalnej w sali nr 44.", "", ""),
        Tweets(4, u"Informujemy, że osoby uprawnione do otrzymania dofinansowania do podręczników szkolnych (II klasa LO), mogą składać wnioski do dyrekcji szkoły najpóźniej do 04. 09. 2013 roku.", u"więcej", ""),

        Tweets(2, u"Marcin Muszalski z klasy 2MAT1 laureatem Ogólnopolskiego Sejmiku Matematyków.", u"", ""),
        Tweets(2, u"31 osób wyróżnionych w konkursie matematycznym Kangur.", u"", ""),
        Tweets(2, u"Wygraliśmy reagaty!", u"", ""),
        TweetsMain(1,1),TweetsMain(2,1),TweetsMain(3,1),TweetsMain(4,2),TweetsMain(5,2),TweetsMain(6,2),
        Videos(2, 2, "68137365"),
        VideosMain(1),
        Sets(2,u"Szoła"),
        Sets(2,u"Edukacja"),
        Sets(2,u"Konkursy"),
        Sets(2,u"Strefa ucznia"),
        SetsItems(2,1,u"Historia szkoły", None, u"/historia-szkoly"),
        SetsItems(2,1,u"Patron", None, u"/patron"),
        SetsItems(2,1,u"Honorowy Patron", None, u"/honorowy-patron"),
        SetsItems(2,1,u"Absolwenci", None, u"/absolwenci-6"),
        SetsItems(2,1,u"Fundacja", None, u"/fundacja"),
        SetsItems(2,1,u"Towarzystwo Szkół Twórczych", None, u"/towarzystwo-szkol-tworczych"),
        SetsItems(2,1,u"Statut Szkoły", None, u"/statut-szkoly"),
        SetsItems(2,1,u"Szkolne Muzeum", None, u"/patron"),
        SetsItems(2,1,u"Regulamin Szkoły", None, u"/patron"),
        SetsItems(2,1,u"Galeria", None, u"/patron"),
        SetsItems(2,1,u"Kontakt", None, u"/patron"),
        SetsItems(2,1,u"Plan lekcji", None, u"/patron"),
        SetsItems(2,1,u"Panorama", None, u"/patron"),
        SetsItems(2,1,u"Staszic na Facebooku", None, u"/patron"),
        SetsItems(2,2,u"Podręczniki", None, u"/podreczniki"),
        SetsItems(2,2,u"Programy nauczania", None, u"/programy_nauczania"),
        SetsItems(2,2,u"Rada Rodziców", None, u"/rada_rodziców"),
        SetsItems(2,2,u"Zebrania", None, u"/zebrania"),
        SetsItems(2,3,u"Z energetyką w przyszłość", None, u"/konkursenergetyka"),
        SetsItems(2,3,u"XIV KRAM Z POEZJĄ", None, u"/konkurs-13-kram-z-poezj"),
        SetsItems(2,3,u"IX OKoP", None, u"/newsy-szkolne/1088-8-okoomaturalny-konkurs-polonistyczny"),
        SetsItems(2,4,u"Tematy Maturalne", None, u"/pliki/matura2014.doc"),
        SetsItems(2,4,u"Bibliografia", None, u"/pliki/bibl.pdf"),
        SetsItems(2,4,u"Comenius", None, u"/comenius"),
        SetsItems(2,4,u"Informatyka", None, u"http://www.ab.staszic.edu.pl/"),
        SetsItems(2,4,u"Poczta", None, u"/poczta/"),
        SetsItems(2,4,u"Konsultacje", None, u"/pliki/KONSULTACJE.pdf"),
        SetsItems(2,4,u"Dyżury klas", None, u"/pliki/dy%C5%BCury.pdf"),
        SetsItems(2,4,u"Dzwonki", None, u"/dzwonki"),
        SetsItems(2,4,u"Czat", None, u"http://czat.staszic.edu.pl/"),
        SetsItems(2,4,u"Szczęśliwy numerek", None, u"http://sis.staszic.edu.pl/lucky"),
        SetsItems(2,4,u"Samorząd uczniowski", None, u"/su"),
        SetsItems(2,4,u"StaszicTV", None, u"/staszictv"),

        EasyLinks(2,"about","/set/1"),
        EasyLinks(2,"education","/set/2"),
        EasyLinks(2,"competitions","/set/3"),
        EasyLinks(2,"student_zone","/set/4"),
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
        LuckyNumbers(datetime.date(2012, 9, 3), 1),
        LuckyNumbers(datetime.date(2012, 9, 4), 2),
        LuckyNumbers(datetime.date(2012, 9, 5), 3),
        LuckyNumbers(datetime.date(2012, 9, 6), 4),
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
        #import_tweets()
        
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

def import_easy_link():
    mypath="./main_page/data/easy_links/"
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
