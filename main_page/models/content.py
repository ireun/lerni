# -*- coding: utf-8 -*-
from .meta import *
####################################################################
###																				  ###
####################################################################
class Folders(Base):		#Dodać dialog button "Poprzednie wersje"#
    __tablename__ = 'folders'		#Wystarczy podpis folderu, który potwierdza poprawność całej reszty #Zrobić pakiet do bezpiecznej publikacji dokumentów#
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    views = Column(Integer)
    state = Column(Boolean)
    date = Column(DateTime)
    gpg_id = Column(Text)
    sign=Column(Text)
    sing_ok=Column(Boolean)
    deleted=Column(Boolean)
    def _get_last(self):
        return self.versions[-1] #object_session(self).query(Address).with_parent(self).filter(...).last()#
    last_version = property(_get_last)
    def __init__(self, user_id, gpg_id=None):
        self.date = datetime.datetime.now()
        self.user_id = user_id
        self.state = False
        self.views = 0
        self.deleted = False
        if gpg_id:
            self.gpg_id = hashlib.sha512("folder"+gpg_id).hexdigest()

class FoldersVersions(Base):
    __tablename__ = "folder_versions"
    id = Column(Integer, primary_key=True)
    folder_id = Column(Integer, ForeignKey('folders.id'))
    folder = relationship("Folders", backref="versions", lazy='subquery')
    title = Column(Text)
    date = Column(DateTime)
    css_id = Column(Integer, ForeignKey('folders_css.id'))
    css = relationship("FoldersCSS")
    tags = Column(Text)
    data_hash = Column(Text)
    def __init__(self, folder_id, title, tags, css_id=None):
        self.folder_id = folder_id
        self.title = title
        self.date = datetime.datetime.now()
        self.css_id = css_id
        self.tags = tags
        self.data_hash = hashlib.sha512(unicode("folder_data"+self.title+tags).encode('utf-8')).hexdigest()

class FoldersCSS(Base):
    __tablename__ = "folders_css"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    versions = relationship("FoldersCSSVersions")
    date = Column(DateTime)
    def __init__(self, user_id):
        self.user_id = user_id
        self.date = datetime.datetime.now()

class FoldersCSSVersions(Base):
    __tablename__ = "folders_css_versions"
    id = Column(Integer, primary_key=True)
    css_id = Column(Integer, ForeignKey('folders_css.id'))
    css = relationship("FoldersCSS")
    name = Column(Text)
    description = Column(Text)
    data = Column(Text)
    date = Column(DateTime)
    data_hash = Column(Text)
    def __init__(self, css_id, name, description, data):
        self.name = name
        self.description = description
        self.data = data
        self.date = datetime.datetime.now()
        self.data_hash = hashlib.sha512(unicode("folder_css"+name+description+data).encode('utf-8')).hexdigest()

class FoldersTags(Base):
    __tablename__ = "folder_tags"
    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'))
    tag = relationship("Tags")
    folder_id = Column(Integer, ForeignKey('folders.id'))
    folder = relationship("Folders")
    state = Column(Boolean)
    def __init__(self, tag_id, folder_id):
        self.tag_id = tag_id
        self.folder_id = folder_id
        self.state = True

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    folders = relationship("FoldersTags")
    entries = relationship("EntriesTags")
    date = Column(DateTime)
    last_used = Column(DateTime)
    def __init__(self,name):
        self.name = name
        self.date = datetime.datetime.now()
        self.last_used = datetime.datetime.now()


class Entries(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    folder_id = Column(Integer, ForeignKey('folders.id'))
    folder = relationship("Folders", backref="entries", lazy='subquery')
    date = Column(DateTime)
    last_update = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted=Column(Boolean)
    def _get_last(self):
        return self.versions[-1] #object_session(self).query(Address).with_parent(self).filter(...).last()#
    last_version = property(_get_last)
    def __init__(self, user_id, folder_id):
        self.user_id = user_id
        self.folder_id = folder_id
        self.date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False

class EntriesVersions(Base):
    __tablename__ = 'entries_versions'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey('entries.id'))
    entry = relationship("Entries", backref="versions", lazy='subquery')
    title = Column(Text)
    text = Column(Text)
    css_id = Column(Integer, ForeignKey('entries_css.id'))
    css = relationship("EntriesCSS")
    date = Column(DateTime)
    tags = Column(Text)
    data_hash = Column(Text)
    def __init__(self, entry_id, title, text, tags, css_id=None):
        self.entry_id = entry_id
        self.title = title
        self.text = text
        self.tags = tags
        self.css_id = css_id
        self.data_hash = hashlib.sha512(unicode("entry_data"+title+text+tags).encode('utf-8')).hexdigest()

class EntriesCSS(Base):
    __tablename__ = "entries_css"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    versions = relationship("EntriesCSSVersions")
    date = Column(DateTime)
    def __init__(self, user_id):
        self.user_id = user_id
        self.date = datetime.datetime.now()

class EntriesCSSVersions(Base):
    __tablename__ = "entries_css_versions"
    id = Column(Integer, primary_key=True)
    css_id = Column(Integer, ForeignKey('entries_css.id'))
    css = relationship("EntriesCSS")
    name = Column(Text)
    description = Column(Text)
    data = Column(Text)
    date = Column(DateTime)
    data_hash = Column(Text)
    def __init__(self, css_id, name, description, data):
        self.name = name
        self.description = description
        self.data = data
        self.date = datetime.datetime.now()
        self.data_hash = hashlib.sha512(unicode("folder_css"+name+description+data).encode('utf-8')).hexdigest()

class EntriesTags(Base):
    __tablename__ = "entries_tags"
    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'))
    tag = relationship("Tags")
    entry_id = Column(Integer, ForeignKey('entries.id'))
    entry = relationship("Entries")
    state = Column(Boolean)
    def __init__(self, tag_id, entry_id):
        self.tag_id = tag_id
        self.entry_id = entry_id
        self.state = True

class EntriesLikes(Base):
    __tablename__ = "entries_likes"
    user_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    user = relationship("People")
    entry_id = Column(Integer, ForeignKey('entries.id'), primary_key=True)
    entry = relationship("Entries")
    date = Column(DateTime)
    last_edit = Column(DateTime)
    number_of_edits = Column(Integer)
    state = Column(Boolean)
    def __init__(self, user_id, entry_id):
        self.user_id = user_id
        self.entry_id = entry_id
        self.date = datetime.datetime.now()
        self.last_edit = datetime.datetime.now()
        self.number_of_edits = 0
        self.state = True

class Presentations(Base):
    __tablename__ = 'presentations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    date = Column(DateTime)
    last_update = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted=Column(Boolean)
    def _get_last(self):
        return self.versions[-1] #object_session(self).query(Address).with_parent(self).filter(...).last()#
    last_version = property(_get_last)
    def __init__(self, user_id):
        self.user_id = user_id
        self.date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False

class PresentationsVersions(Base):
    __tablename__ = 'presentations_versions'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey('presentations.id'))
    entry = relationship("Presentations", backref="versions", lazy='subquery')
    title = Column(Text)
    text = Column(Text)
    css_id = Column(Integer, ForeignKey('entries_css.id'))
    css = relationship("EntriesCSS")
    date = Column(DateTime)
    tags = Column(Text)
    data_hash = Column(Text)
    def __init__(self, entry_id, title, text, tags, css_id=None):
        self.entry_id = entry_id
        self.title = title
        self.text = text
        self.tags = tags
        self.css_id = css_id
        self.data_hash = hashlib.sha512(unicode("entry_data"+title+text+tags).encode('utf-8')).hexdigest()

class Tweets(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    date = Column(DateTime)
    last_update = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted=Column(Boolean)
    text=Column(Text)
    link=Column(Text)
    link_name=Column(Text)
    def __init__(self, user_id, text, link, link_name):
        self.user_id = user_id
        self.date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False
        self.text = text
        self.link = link
        self.link_name = link_name

class TweetsMain(Base):
    __tablename__ = 'tweets_main'
    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer, ForeignKey('tweets.id'))
    tweet = relationship("Tweets")
    category_id = Column(Integer, ForeignKey('tweets_categories.id'))
    category = relationship("TweetsCategories")
    #confirmed = Column(Boolean)
    #confirmation_id
    confirm = Column(Integer, ForeignKey('people.id'))
    def __init__(self, tweet_id, category_id):
        self.tweet_id = tweet_id
        self.category_id = category_id

class TweetsCategories(Base):
    __tablename__ = 'tweets_categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    maintener_id = Column(Integer, ForeignKey('people.id'))
    maintener = relationship("People")
    def __init__(self, name, maintener_id=None):
        self.name = name
        self.maintener_id = maintener_id


class Videos(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    date = Column(DateTime)
    last_update = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted=Column(Boolean)
    hosting_id=Column(Integer) #1-youtube 2-vimeo
    link=Column(Text)
    def __init__(self, user_id, hosting_id, link):
        self.user_id = user_id
        self.date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False
        self.hosting_id = hosting_id
        self.link = link

class VideosMain(Base):
    __tablename__ = 'videos_main'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey('videos.id'))
    video = relationship("Videos")
    confirm1 = Column(Integer, ForeignKey('people.id'))
    confirm2 = Column(Integer, ForeignKey('people.id'))
    def __init__(self, video_id):
        self.video_id = video_id

class Banners(Base):
    __tablename__ = 'banners'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    date = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted = Column(Boolean)
    link=Column(Text)
    alternative=Column(Text)
    def __init__(self, user_id, start_date, end_date, link, alternative):
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.link = link
        self.alternative = alternative
        self.date = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False
class Sets(Base):
    __tablename__ = 'sets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    date = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted = Column(Boolean)
    name=Column(Text)
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.date = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False

class SetsItems(Base):
    __tablename__ = 'sets_items'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    set_id = Column(Integer, ForeignKey('sets.id'))
    set = relationship("Sets", backref="items", lazy='subquery')
    date = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted = Column(Boolean)
    name=Column(Text)
    thumb=Column(Text)
    link=Column(Text)
    def __init__(self, user_id, set_id, name, thumb, link):
        self.user_id = user_id
        self.set_id = set_id
        self.name = name
        self.link = link
        self.date = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False

class EasyLinks(Base):
    __tablename__ = "easy_links"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('people.id'))
    user = relationship("People")
    date = Column(DateTime)
    views = Column(Integer)
    state = Column(Boolean)
    deleted = Column(Boolean)
    name=Column(Text)
    path=Column(Text)
    def __init__(self, user_id, name, path):
        self.user_id = user_id
        self.name = name
        self.path = path
        self.date = datetime.datetime.now()
        self.views = 0
        self.state = False
        self.deleted = False

class LuckyNumbers(Base):
    __tablename__ = 'lucky_numbers'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    number = Column(Integer)

    def __init__(self, date, number):
        self.date = date
        self.number = number

# Do usunięcia
#class Articles_Comments(Base):
#    __tablename__ = 'articles_comments'
#    id = Column(Integer, primary_key=True)
#    article_id = Column(Integer, ForeignKey('articles.id'))
#    add_date = Column(DateTime)
#    author_id = Column(Integer, ForeignKey('people.id'))
#    content = Column(Text)

#    def __init__(self, article_id, add_date, author_id, content):
#        self.article_id = article_id
#        self.add_date = add_date
 #       self.author_id = author_id
 #       self.content = content
