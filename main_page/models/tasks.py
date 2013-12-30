from .meta import *

class TaskItem(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(Text, unique=True)