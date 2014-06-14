from .meta import *


class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Text)

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Cache(Base):
    __tablename__ = 'cache'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Text)
    date = Column(DateTime)

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.date = datetime.datetime.now()