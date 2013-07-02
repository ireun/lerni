from .meta import *
class MenuTop(Base):
    __tablename__ = 'menu_top'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    link = Column(Text)

    def __init__(self, name, link):
        self.name = name
        self.link = link
        
class MenuLeft(Base):
    __tablename__ = 'menu_left'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    link = Column(Text)

    def __init__(self, name, link):
        self.name = name
        self.link = link