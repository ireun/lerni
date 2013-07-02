from .meta import *
class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    add_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey('people.id'))
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
class ArticlesMainPage(Base):
    __tablename__ = 'articles_mainpage'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article = relationship("Articles")
    confirm1 = Column(Integer, ForeignKey('people.id'))
    confirm2 = Column(Integer, ForeignKey('people.id'))
    def __init__(self, article_id, confirm1, confirm2):
        self.article_id = article_id
        self.confirm1 = confirm1
        self.confirm2 = confirm2
    
class ArticlesContent(Base):
    __tablename__ = 'articles_content'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    title = Column(Text)
    add_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey('people.id'))
    content = Column(Text)
    def __init__(self, article_id, title, content, add_date, author_id):
        self.title = title
        self.content = content
        self.add_date = add_date
        self.author_id = author_id

class Articles_Comments(Base):
    __tablename__ = 'articles_comments'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    add_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey('people.id'))
    content = Column(Text)

    def __init__(self, article_id, add_date, author_id, content):
        self.article_id = article_id
        self.add_date = add_date
        self.author_id = author_id
        self.content = content
        
class ArticlesCategories(Base):
    __tablename__ = 'articles_categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text)    
    def __init__(self, name):
        self.name = name
        