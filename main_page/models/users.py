from .meta import *
class Titles(Base):
    __tablename__ = 'titles'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    def __init__(self, name):
        self.name = name      
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    second_name = Column(Text)
    last_name = Column(Text)
    pesel = Column(Text)
    occupation_id = Column(Integer, ForeignKey('occupations.id'))
    
    title_id = Column(Integer, ForeignKey('titles.id'))
    login = Column(Text)
    username = Column(Text)
    password = Column(Text)
    email = Column(Text)
    classes = relationship("Association")
    group_id = Column(Integer, ForeignKey('users_groups.id'))    
    def __init__(self, first_name, second_name, last_name, pesel, occupation_id, title_id, login, username, password, email, group_id):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.pesel = pesel
        self.occupation_id = occupation_id
        self.title_id = title_id
        self.login = login
        self.password = password
        self.username = username
        self.email = email
        self.group_id = group_id
        
class Users_Groups(Base):
    __tablename__ = 'users_groups'
    id = Column(Integer, primary_key=True)
    name = Column(Text)    
    def __init__(self, name):
        self.name = name
        
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
    ALL_PERMISSIONS
    )
class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:super_admin', ALL_PERMISSIONS),
                (Allow, 'group:dyrektor', 'dyrektor'),
                (Allow, 'group:teacher', 'oceny'),
                (Allow, 'group:admin', 'edit_articlesa'),
                (Allow, 'group:redaktor', 'edit_articles'),
                (Allow, 'group:student', ('view_subs','edit')), 
                (Allow, 'group:basic', 'edit') ]
    def __init__(self, request):
        pass