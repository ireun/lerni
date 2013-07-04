from .meta import *
class Tweets(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    add_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey('people.id'))
    state = Column(Boolean)
    category_id = Column(Integer, ForeignKey('articles_categories.id'))
    category = relationship("ArticlesCategories")
    content = Column(Text)
    def __init__(self, add_date, author_id, state, category_id, content):
        self.add_date = add_date
        self.author_id = author_id
        self.state = state
        self.category_id = category_id
        self.content = content
        
class TweetsCategories(Base):
    __tablename__ = 'tweets_categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text)    
    def __init__(self, name):
        self.name = name