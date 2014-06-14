# -*- coding: utf-8 -*-
from .meta import *


class SyllabusYears(Base):
    __tablename__ = 'syllabus_years'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    path_name = Column(Text)
    add_date = Column(Date)
    modification_date = Column(Date)
    profiles = relationship("SyllabusProfiles", cascade="all,delete", lazy='dynamic')

    def __init__(self, name, path_name):
        self.name = name
        self.path_name = path_name
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


class SyllabusProfiles(Base):
    __tablename__ = 'syllabus_profiles'
    id = Column(Integer, primary_key=True)
    syllabus_id = Column(Integer, ForeignKey('syllabus_years.id'))
    syllabus = relationship("SyllabusYears")
    name = Column(Text)
    path_name = Column(Text)
    description = Column(Text)
    add_date = Column(Date)
    modification_date = Column(Date)
    extensions = relationship("SyllabusExtensions", cascade="all,delete", lazy='dynamic')

    def __init__(self, name, path_name, description):
        self.name = name
        self.path_name = path_name
        self.description = description
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()


class SyllabusExtensions(Base):
    __tablename__ = 'syllabus_extansions'
    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('syllabus_profiles.id'))
    profile = relationship("SyllabusProfiles")
    name = Column(Text)
    path_name = Column(Text)
    description = Column(Text)
    add_date = Column(Date)
    modification_date = Column(Date)

    def __init__(self, name, path_name, description):
        self.name = name
        self.path_name = path_name
        self.description = description
        self.add_date = datetime.datetime.now()
        self.modification_date = datetime.datetime.now()