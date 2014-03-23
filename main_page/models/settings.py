from .meta import *


class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Text)

    def __init__(self, name, value):
        self.name = name
        self.value = value