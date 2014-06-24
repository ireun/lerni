from .meta import *


class Files(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    fileData = Column(Text)
    fileid = Column(Integer, unique=True)
    token = Column(Text)
    original_filename = Column(Text)
    md5_hash = Column(Text)
    add_time = Column(DateTime)
    uploaded = Column(Boolean)

    def __init__(self, file_data, fileid, token, original_filename, md5_hash, add_time):
        self.fileData = file_data
        self.fileid = fileid
        self.token = token
        self.original_filename = original_filename
        self.md5_hash = md5_hash
        self.add_time = add_time
        self.uploaded = False