from .meta import *
class FlashCategories(Base):
    __tablename__ = 'flash_categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text) # Nazwa decku
    
    
    
    add_date = Column(DateTime)
    state = Column(Boolean)
    sticked = Column(Boolean)
    category_id = Column(Integer, ForeignKey('articles_categories.id'))
    category = relationship("ArticlesCategories")
    hits = Column(Integer)    
    def __init__(self, add_date, author_id,state,sticked,category_id,hits):
        self.add_date = add_date
        self.author_id = author_id
        self.state = state
        self.sticked = sticked
        self.category_id = category_id
        self.hits = hits
class FlashDecks(Base):
    __tablename__ = 'flash_decks'
    id = Column(Integer, primary_key=True)
    front = Column(Text)
    back = Column(Text)
    
    
    add_date = Column(DateTime)
    state = Column(Boolean)
    sticked = Column(Boolean)
    category_id = Column(Integer, ForeignKey('articles_categories.id'))
    category = relationship("ArticlesCategories")
    hits = Column(Integer)    
    def __init__(self, add_date, author_id,state,sticked,category_id,hits):
        self.add_date = add_date
        self.author_id = author_id
        self.state = state
        self.sticked = sticked
        self.category_id = category_id
        self.hits = hits