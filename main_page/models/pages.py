from .meta import *
class Pages(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    url_name = Column(Text, unique=True)
    name = Column(Text)
    sub_pages = relationship("SubPages")
    def __init__(self, url_name, name):
        self.url_name = url_name
        self.name = name

class SubPages(Base):
    __tablename__ = 'sub_pages'
    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey('pages.id'))
    url_name = Column(Text)
    name = Column(Text)    
    data = Column(Text)    
    def __init__(self, page_id, url_name, name, data):
        self.page_id = page_id
        self.url_name = url_name
        self.name = name
        self.data = data
        
class Competitors(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    competition_group_id = Column(Integer, ForeignKey('competitors_groups.id'))
    competition_group = relationship("CompetitorsGroups")
    competition_id = Column(Integer, ForeignKey('competitors_competitions.id'))
    competition = relationship("CompetitorsCompetitions")
    competitor_type_id = Column(Integer, ForeignKey('competitors_types.id'))
    competitor_type = relationship("CompetitorsTypes")
    competitor_tutor_id = Column(Integer, ForeignKey('competitors_tutors.id'))
    competitor_tutor = relationship("CompetitorsTutors")
    start_year = Column(Integer) #Start of school year
    end_year = Column(Integer)
    
    def __init__(self, first_name, last_name, competition_id, competitor_type_id, competitor_tutor_id, start_year, end_year, competition_group_id):
        self.first_name = first_name
        self.last_name = last_name
        self.competition_id = competition_id
        self.competitor_type_id = competitor_type_id
        self.competitor_tutor_id = competitor_tutor_id
        self.start_year = start_year
        self.end_year = end_year
        self.competition_group_id = competition_group_id
        
class CompetitorsGroups(Base):
    __tablename__ = 'competitors_groups'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")
    def __init__(self, name):
        self.name = name
        
class CompetitorsCompetitions(Base):
    __tablename__ = 'competitors_competitions'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")
    def __init__(self, name):
        self.name = name
        
class CompetitorsTypes(Base):
    __tablename__ = 'competitors_types'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")
    def __init__(self, name):
        self.name = name
        
class CompetitorsTutors(Base):
    __tablename__ = 'competitors_tutors'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    competitors = relationship("Competitors")
    def __init__(self, name):
        self.name = name
        
        