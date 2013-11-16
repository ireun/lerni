# -*- coding: utf-8 -*-
from .meta import *


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    second_name = Column(Text)
    last_name = Column(Text)
    pesel = Column(Text)
    birth_date = Column(DateTime)
    phone_number = Column(Text)
    email = Column(Text)
    password = Column(Text)
    password_date = Column(DateTime)
    password_force_update = Column(Boolean)
    key_data = Column(Text)
    fingerprint = Column(Text)
    teacher = relationship("Teachers")
    student = relationship("Students")
    officials = relationship("Officials")
    aalogins = relationship("AALogin")
    wallet_id = Column(Integer, ForeignKey('wallet.id'), unique=True)
    wallet = relationship("Wallet")
    email_confirmed = Column(Boolean)
    gpg_confirmed = Column(Boolean)
    phone_confirmed = Column(Boolean)
    registration_date = Column(DateTime)
    last_login = Column(DateTime)
    is_male = Column(Boolean)
    bitcoin = Column(Text)
    web_page = Column(Text)
    title = Column(Text)
    group_id = Column(Integer)
    folders = relationship("Folders", lazy="dynamic")
    folders_css = relationship("FoldersCSS", lazy="dynamic")
    entries_css = relationship("EntriesCSS", lazy="dynamic")
    entries_likes = relationship("EntriesLikes", lazy="dynamic")

    def _get_full_name(self):
        return self.first_name+" "+self.last_name
    full_name = property(_get_full_name)

    def __init__(self, first_name, second_name, last_name, pesel, birth_date, phone_number, email, password, key_data,
                 fingerprint, wallet_id, email_confirmed, gpg_confirmed, phone_confirmed, group_id):
        self.registration_date = datetime.datetime.now()
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.pesel = pesel
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.email = email
        self.password = hashlib.sha512(unicode(password+str(self.registration_date)).encode('utf-8')).hexdigest()
        self.password_date = datetime.datetime.now()
        self.password_force_update = False
        self.key_data = key_data
        self.fingerprint = fingerprint
        self.wallet_id = wallet_id
        self.email_confirmed = email_confirmed
        self.gpg_confirmed = gpg_confirmed
        self.phone_confirmed = phone_confirmed
        self.is_male = True
        self.group_id = group_id

    def check_password(self, passwd):
        return self.password == hashlib.sha512(unicode(passwd+str(self.registration_date)).encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User %r>' % (self.first_name+" "+self.last_name).strip()

    def __str__(self):
        return (self.first_name+" "+self.last_name).strip()


class AALogin(Base):
    __tablename__ = 'account_activity_login'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    client_addr = Column(Text)
    user_agent = Column(Text)
    accept_language = Column(Text)
    date = Column(DateTime)

    def __init__(self, user_id, client_addr, user_agent, accept_language, date):
        self.user_id = user_id
        self.client_addr = client_addr
        self.user_agent = user_agent
        self.accept_language = accept_language
        self.date = date


class Teachers(Base):
    __tablename__ = 'log_teachers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'), unique=True)
    user = relationship("People")
    state = Column(Integer)

    #1 - waiting for acceptation, 2 - working, 3 - ended work
    def __init__(self, user_id, state=1):
        self.user_id = user_id
        self.state = state


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")

    def __init__(self, user_id):
        self.user_id = user_id


class Officials(Base):
    __tablename__ = 'officials'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'), unique=True)
    user = relationship("People")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    state = Column(Integer)

    def __init__(self, user_id, state=1):
        self.user_id = user_id
        self.start_date = datetime.datetime.now()
        self.state = state


class AppCodes(Base):
    __tablename__ = 'app_codes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    phone_name = Column(Text)
    phone_id = Column(Text)
    code = Column(Text)

    def __init__(self, user_id, phone_name, phone_id, code):
        self.user_id = user_id
        self.phone_name = phone_name
        self.phone_id = phone_id
        self.code = code

from pyramid.security import (
    Allow,
    Everyone,
    ALL_PERMISSIONS)


class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:super_admin', ALL_PERMISSIONS),
               (Allow, 'group:dyrektor', 'dyrektor'),
               (Allow, 'group:teacher', 'oceny'),
               (Allow, 'group:admin', 'edit_articlesa'),
               (Allow, 'group:redaktor', 'edit_articles'),
               (Allow, 'group:student', ('view_subs', 'edit')),
               (Allow, 'group:basic', ('account_settings', 'edit'))]

    def __init__(self, request):
      pass