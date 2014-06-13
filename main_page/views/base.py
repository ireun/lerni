# -*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config

import transaction
import datetime
import time
import linecache
import uuid
import hashlib
import random
import re

from recaptcha.client import captcha

from sqlalchemy.exc import DBAPIError, OperationalError
from sqlalchemy import or_
import locale
from sqlalchemy import desc
from sqlalchemy import asc
from main_page.models import (DBSession,
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
                              TweetsCategories,
                              TweetsCategoriesList,
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
                              Bells,
                              BellsTypes,
                              Graduates,
                              Competitors,
                              CompetitorsCompetitions,
                              CompetitorsTutors,
                              CompetitorsTypes,
                              CompetitorsGroups,
                              Files,
                              PingResults,
                              PingIPs,
                              Settings,
                              ArticlesProposed
                              )
    
#import re
#from docutils.core import publish_parts

from pyramid.httpexceptions import (
                                    HTTPFound,
                                    HTTPNotFound,
                                    exception_response,
                                    )
    
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    has_permission,
    )
from math import ceil
   
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
from pyramid_mailer.message import Attachment

from itsdangerous import URLSafeSerializer, TimestampSigner, BadSignature, BadData, SignatureExpired
secret = 'secret-key'
recaptcha_private = "6Lfz3OUSAAAAANh7eynb6CW4aehuKxK6yLgnPRg8"
recaptcha_public = "6Lfz3OUSAAAAACtP35cn21roRF4k9eS5Tw6c6ik2"
import os
import gnupg
from pprint import pprint
#gpg = gnupg.GPG(gnupghome='GPG')


from BeautifulSoup import BeautifulSoup
import json
import pdfkit
from pyramid.renderers import render
import tempfile
from contextlib import contextmanager
import string
valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
import bbcode

from main_page.tasks import ping
import urllib2
import celery
from socket import error as socket_error
import errno


@contextmanager
def tempinput(data):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    temp.write(data.encode('utf8'))
    temp.close()
    yield temp.name
    os.unlink(temp.name)


def pl_to_ascii(text):
    pl = {ord(u'Ą'): u'A', ord(u'Ć'): u'C', ord(u'Ę'): u'E', ord(u'Ł'): u'L', ord(u'Ó'): u'O', ord(u'Ś'): u'S',
          ord(u'Ź'): u'Z', ord(u'Ż'): u'Z',
          ord(u'ą'): u'a', ord(u'ć'): u'c', ord(u'ę'): u'e', ord(u'ł'): u'l', ord(u'ó'): u'o', ord(u'ś'): u's',
          ord(u'ź'): u'z', ord(u'ż'): u'z'}
    return text.translate(pl)


def response_pdf(request, html, filename):
    response = request.response
    with tempinput(html) as tempfilename:
        with tempinput("") as output_file:
            #wk = pdfkit.from_file(tempfilename, output_file)
            #,dpi="300",screen_resolution=[1280, 1024])
            response.body_file = pdfkit.from_file('test.html', False)
            response.content_type = 'application/pdf'
            filename = filename.replace(" ", "_")
            filename = pl_to_ascii(filename)
            filename = ''.join(c for c in filename if c in valid_chars).strip(".")
            response.headerlist.append(("Content-Disposition", "attachment; filename='"+str(filename)+".pdf'"))
            return response


def username(logged_in):
    try:
        name = ""
        if logged_in:
            name = DBSession.query(People).filter_by(email=logged_in).first().first_name
    except DBAPIError:
        return Response("Mysql connection error", content_type='text/plain', status_int=500)
    return name


def setting_save(name, value):
    session = DBSession()
    try:
        setting = DBSession.query(Settings).filter_by(name=name).first()
        setting.value = value
    except AttributeError:
        setting = Settings(name, value)
        session.add(setting)
    transaction.commit()
    return True


def setting_load(name):
    return DBSession.query(Settings).filter_by(name=name).first().value


def send_mail(request, subject, recipients, body, fingerprint=False):
    #if fingerprint:
    #    body=str(gpg.encrypt(body, fingerprint, always_trust=True))
    mailer = request.registry['mailer']
    message = Message(subject=subject,
                      sender="mailer.staszic@gmail.com",
                      recipients=recipients,
                      body=body)
    mailer.send_immediately(message)


parser = bbcode.Parser(normalize_newlines=False, install_defaults=False, escape_html=False, replace_links=False, replace_cosmetic=False)
parser.add_simple_formatter('hr', '<hr />', standalone=True)
parser.add_simple_formatter('br', '<br />')
parser.add_simple_formatter('p', '<p>%(value)s</p>')
parser.add_simple_formatter('diagram', '<div class="diagram">%(value)s</div>')
parser.add_simple_formatter('date', '<abbr class="timeago" title="%(value)s">%(value)s</abbr>')


def render_widget(tag_name, value, options, parent, context):
    return render('widgets/'+tag_name+'.mak', dict(list(options.items()) + list({'value':value}.items())))
for widget in ("map", "vimeo", 'support'):
    parser.add_formatter(widget, render_widget)


def last_video(tag_name, value, options, parent, context):
    last_video = DBSession.query(VideosMain).order_by('-id').first().video
    if last_video.hosting_id == 1:
        return ""
    elif last_video.hosting_id == 2:
        return render('widgets/vimeo.mak', {'value': last_video.link})
parser.add_formatter("last_video", last_video)


def tweets(tag_name, value, options, parent, context):
    to_return=""
    c = DBSession.query(TweetsCategoriesList).filter_by(name=value).first()
    for position in DBSession.query(TweetsCategories).order_by('-id').filter_by(category=c).limit(8):
        to_return += "<div class='article'>"
        to_return += "<div class='author'>"+position.tweet.user.full_name+"</div>"
        to_return += "<div class='timeago' title='"+str(position.tweet.date)+"'></div> <br>"
        to_return += "<div class='content'>"+position.tweet.text
        if position.tweet.link != None:
            to_return += "<a href='"+position.tweet.link+"'>"+position.tweet.link_name+"</a>"
        to_return += "</div></div>"
    return to_return
parser.add_formatter("tweets", tweets)


def status(tag_name, value, options, parent, context):
    page = {}
    page['services'] = []
    for x in value.split("|"):
        page['services'].append([x.split(",")[0]])
        for y in x.split(",")[1:]:
            try:
                service_id = DBSession.query(PingIPs).filter_by(name=y).first().id
                service_status = DBSession.query(PingResults).filter_by(ip_id=service_id). \
                    order_by(PingResults.date.desc()).first().result
            except ValueError:
                service_status = None
            page['services'][-1].append(service_status)
    to_return = render('widgets/status.mak', page)
    return to_return


parser.add_formatter("status", status)


def successes(tag_name, value, options, parent, context):
    to_return = render('widgets/competitors.mak', {})
    return to_return
parser.add_formatter("successes", successes)


def youtube(tag_name, value, options, parent, context):
    to_return = render('widgets/youtube.mak', {'value': value})
    return to_return
parser.add_formatter("youtube", youtube)


def graduates(tag_name, value, options, parent, context):
    to_return = render('widgets/graduates.mak',{})
    return to_return
parser.add_formatter("graduates", graduates)


def bells(tag_name, value, options, parent, context):
    c = DBSession.query(Bells).join(BellsTypes).filter(BellsTypes.name.in_([value]))
    bl=[]
    for position in c:
        bl.append([position.order, position.start.strftime("%H:%M"), position.end.strftime("%H:%M")])
    to_return = render('widgets/bells.mak',{'bl': bl})
    return to_return
parser.add_formatter("bells", bells)


def get_week(day):
    start = day-datetime.timedelta(day.weekday())
    end = day+datetime.timedelta(6-day.weekday())
    return start, end


def lucky_numbers(tag_name, value, options, parent, context):
    page={}
    lucky_number = DBSession.query(LuckyNumbers).filter_by(date=datetime.datetime.now().date()+datetime.timedelta(1))
    lucky_number = lucky_number.first()
    try:
        page['lucky_number'] = lucky_number.number
        page['lucky_number_date'] = lucky_number.date
    except AttributeError:
        page['lucky_number'] = "??"
        page['lucky_number_date'] = ""
    week = get_week(datetime.datetime.now().date()+datetime.timedelta(1))
    page['numbers'] = []
    for x in DBSession.query(LuckyNumbers).filter(LuckyNumbers.date.between(week[0], week[1])):
        page['numbers'].append([x.date, x.number])
    all_numbers = range(37)
    all_numbers.remove(0)
    for x in DBSession.query(LuckyNumbers).order_by(asc(LuckyNumbers.date)):
        if x.number in all_numbers:
            all_numbers.remove(x.number)
        else:
            all_numbers = range(37)
            all_numbers.remove(0)
    page['left'] = sorted(all_numbers)
    to_return = render('widgets/lucky.mak',page)
    return to_return
parser.add_formatter("lucky_numbers", lucky_numbers)

def get_basic_account_info(request):
    page = {}
    page['logged_in'] = authenticated_userid(request)
    page['name'] = username(page['logged_in'])
    page['balance_history'] = ",".join(["0", "0", "0", "0", "0", "0", "0", "0", "0"])
    page['balance'] = 0
    page['likes_history'] = ",".join(["0", "0", "0", "0", "0", "0", "0", "0", "0"])
    page['likes'] = 0
    page['subscribers_history'] = ",".join(["0", "0", "0", "0", "0", "0", "0", "0", "0"])
    page['subscribers'] = 0
    page['preparation_history'] = ",".join(["100", "100", "100", "100", "100", "100", "100", "100", "100"])
    page['preparation'] = 100
    return page


def timetable(tag_name, value, options, parent, context):
    #return u'<table class="table table-striped"><tr><td> Plan lekcji pojawi się, gdy uzupełnisz swoje dane (klasa,lektorat/uczone klasy) </tr></td></table>'
    page = {}
    page['lessons'] = [['1', [], [], [], [], []], ['2', [], [], [], [], []],
                       ['3', [], [], [], [], []], ['4', [], [], [], [], []],
                       ['5', [], [], [], [], []], ['6', [], [], [], [], []],
                       ['7', [], [], [], [], []], ['8', [], [], [], [], []]]
    page['lessons2'] = [['1', [], [], [], [], []], ['2', [], [], [], [], []],
                       ['3', [], [], [], [], []], ['4', [], [], [], [], []],
                       ['5', [], [], [], [], []], ['6', [], [], [], [], []],
                       ['7', [], [], [], [], []], ['8', [], [], [], [], []]]

    if 'teacher' in options:
        page['who'] = options['teacher']
        t = page['who']
        teacher = DBSession.query(People).filter_by(first_name=t.split(" ")[0], last_name=t.split(" ")[1])
        teacher = DBSession.query(Teachers).filter_by(user_id=teacher.first().id).first()
        for position in DBSession.query(Lessons).filter_by(teacher_id=teacher.id):
            for x in DBSession.query(LessonsGroups).filter_by(lesson_id=position.id):
                page['lessons'][position.order-1][position.day+1].append(x.group.name)
                page['lessons2'][position.order-1][position.day+1].append(x.group.name)
            for x in page['lessons2'][position.order-1][position.day+1]:
                division=DBSession.query(Groups).filter_by(name=x).first().division
                all_groups=[]
                for y in DBSession.query(Groups).filter_by(division_id=division.id):
                    all_groups.append(y.name)
                if set(all_groups) <= set(page['lessons'][position.order-1][position.day+1]):
                    for z in all_groups:
                        page['lessons'][position.order-1][position.day+1].remove(z)
                    page['lessons'][position.order-1][position.day+1].append(division.name)
            page['lessons'][position.order-1][position.day+1][-1] += "["+str(position.room)+"]"
            #    page['lessons'][position.order-1][position.day+1][0].append(x.group.name)
    elif 'group' in options:
        page['who'] = options['group']
        division = DBSession.query(Divisions).filter_by(name=page['who']).first()
        g_id=0
        for group in DBSession.query(Groups).filter_by(division_id=division.id):
            for x in range(8):
                for y in range(5):
                    page['lessons'][x][y+1].append("---")

            for p in DBSession.query(LessonsGroups).filter_by(group_id=group.id):
                if p.lesson.subject.name:
                    s_name = p.lesson.subject.name
                else:
                    s_name = "unknown"
                page['lessons'][p.lesson.order-1][p.lesson.day][g_id] = s_name+"[" + str(p.lesson.room) + "]"
            g_id += 1
        for order in range(len(page['lessons'])):
            for lesson in range(len(page['lessons'][order])):
                l = page['lessons'][order][lesson]
                if len(l) == 2 and l[0] == l[1]:
                    page['lessons'][order][lesson] = [l[0]]
    #else:
    #    return "error"
    return render('widgets/timetable.mak', page)
parser.add_formatter("timetable", timetable)