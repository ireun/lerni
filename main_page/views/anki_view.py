# -*- coding: utf-8 -*-
from base import *
import anki
from anki.sync import Syncer, MediaSyncer
from anki.utils import intTime, checksum
from anki.consts import SYNC_ZIP_SIZE, SYNC_ZIP_COUNT
import json
from StringIO import StringIO
import gzip

@view_config(route_name='sync_host_key', renderer='jsonp')
def anki_sync_host_key(request):
    l = json.loads
    d = json.dumps
    compression = request.params['c']
    fs = request.params['data'].file
    if compression:
        fs = gzip.GzipFile(mode="rb", fileobj=fs, compresslevel=1)
    data = fs.read()
    print data
    return {'key': 'my_anki_key'}

@view_config(route_name='sync_download', renderer='jsonp')
def anki_sync_download(request):
    l = json.loads
    d = json.dumps
    compression = request.params['c']
    for x in request.params:
        print x
    fs = request.params['data'].file
    if compression:
        fs = gzip.GzipFile(mode="rb", fileobj=fs, compresslevel=1)
    data = fs.read()
    print data

@view_config(route_name='anki_sync_meta', renderer='jsonp')
def anki_sync(request):
    #c, k, data
    print request.params['data']
    return {'scm': "self.col.scm",
            'ts': intTime(),
            'mod': "self.col.mod",
            'usn': "self.col._usn",
            'musn': "self.col.media.usn()",
            'msg': '',
            'cont': True}

@view_config(route_name='anki_sync_upload', renderer='jsonp')
def anki_syncupload(request):
    filename = request.params['data'].filename
    input_file = request.params['data'].file

    file_path = os.path.join('/tmp', '%s.mp3' % uuid.uuid4())
    temp_file_path = file_path + '~'
    output_file = open(temp_file_path, 'wb')


    input_file.seek(0)
    while True:
        data = input_file.read(2<<16)
        if not data:
            break
        output_file.write(data)
    output_file.close()
    os.rename(temp_file_path, file_path)
    return {'scm': "self.col.scm",
            'ts': intTime(),
            'mod': "self.col.mod",
            'usn': "self.col._usn",
            'musn': "self.col.media.usn()",
            'msg': '',
            'cont': True}

@view_config(route_name='sync_media_list', renderer='jsonp')
def anki_sync_media_list(request):
    for x in request.params:
        print x
    #print request.params['data']
    return {'scm': "self.col.scm",
            'ts': intTime(),
            'mod': "self.col.mod",
            'usn': "self.col._usn",
            'musn': "self.col.media.usn()",
            'msg': '',
            'cont': True}

@view_config(route_name='sync_remove', renderer='jsonp')
def anki_sync_remove(request):
    for x in request.params:
        print x
    print request.params['data']
    return {'scm': "self.col.scm",
            'ts': intTime(),
            'mod': "self.col.mod",
            'usn': "self.col._usn",
            'musn': "self.col.media.usn()",
            'msg': '',
            'cont': True}

@view_config(route_name='sync_files', renderer='jsonp')
def anki_sync_remove(request):
    for x in request.params:
        print x
    print request.params['data']
    return {'scm': "self.col.scm",
            'ts': intTime(),
            'mod': "self.col.mod",
            'usn': "self.col._usn",
            'musn': "self.col.media.usn()",
            'msg': '',
            'cont': True}