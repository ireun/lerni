# -*- coding: utf-8 -*-
from base import *
import os
import uuid
import re
import md5   #Zastapic hashlib
import random
import time

filepath="/home/kamil/test_upload/"
packet_size=512*512
store_files=True

@view_config(route_name='file_upload', renderer='jsonp')
def store_mp3_view(request):
    if len(request.POST) == 0 and len(request.GET) == 0:
        return {"error":"No post request"}
    if len(request.GET) == 0:
        if request.POST.has_key('totalSize') and request.POST.has_key('type') and request.POST.has_key('fileName') and request.POST.has_key('totalSize'): #is_numeric($_POST['totalSize']))
            return newUpload(request)
        elif request.POST['fileid'] and request.POST['token']: # && preg_match('/[A-Za-z0-9]/', $_POST['token'])
            return mergeFiles(request)
    else:
        if request.GET['fileid'] and request.GET['token'] and request.GET['packet']: #type(request.GET['packet']): is_numeric($_GET['packet']) && is_numeric($_GET['fileid'])) {
            return getPacket(request)

def newUpload(request):
    fileData = str(request.POST['totalSize'])+"|"+re.sub('/[^A-Za-z0-9\/]/', '', request.POST['type'])+"|"+re.sub('/[^A-Za-z0-9\/]/', '', request.POST['fileName'])
    originalFileName = request.POST['fileName'];
    token = md5.new(fileData).hexdigest()
    x=1
    while x:
        fileid=str(time.time())+str(random.randint(5, pow(2, 31) - 1))
        if DBSession.query(Files).filter_by(fileid=fileid).count()==0:
            x=0
    with transaction.manager:
        DBSession.add_all([Files(fileData, fileid, token, originalFileName, "", datetime.datetime.now()) ])
    return {"action":"new_upload","fileid":fileid,"token":token}
  
def getPacket(request):
    if DBSession.query(Files).filter_by(fileid=request.GET['fileid']).filter_by(token=request.GET['token']).count()!=0:
        if store_files:
            filename = request.GET['fileid']+"-"+request.GET['packet']
            input_file = request.POST['data'].file
            file_path = filepath+filename
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
        return {"action":"new_packet","result":"success","packet":request.GET['packet']}
        
def mergeFiles(request):
    if DBSession.query(Files).filter_by(fileid=request.POST['fileid']).filter_by(token=request.POST['token']).count()==0:
        return {"error":"No file found in the database for the provided ID / token"}
    exists=1
    try:
        with open(filepath+request.POST['fileid']): pass
    except IOError:
        exists=0
    if not exists:
        fileDataList=DBSession.query(Files).filter_by(fileid=request.POST['fileid']).filter_by(token=request.POST['token']).first().fileData.split("|")
        fileSize=fileDataList[0]
        fileType=fileDataList[1]
        fileName=fileDataList[2]

        totalPackages = ceil(float(fileSize)/packet_size);

        for package in range(int(totalPackages)):
            exists=1
            try:
                with open(filepath+request.POST['fileid']+"-"+str(package)): pass
            except IOError:
                exists=0
            if not exists:
                return {"error":"Missing package #"+package}
                
        output_file = open(filepath+request.POST['fileid'], 'ab') ## Wyjątki dorobić throwError("Unable to create new file for merging");
        
        file_hash = md5.new()
        for package in range(int(totalPackages)):
            input_file=open(filepath+request.POST['fileid']+"-"+str(package),'rb')
            input_data=input_file.read()
            output_file.write(input_data)
            file_hash.update(input_data)
            input_file.close()
            os.remove(filepath+request.POST['fileid']+"-"+str(package))
        output_file.close()    
        DBSession.query(Files).filter_by(fileid=request.POST['fileid']).filter_by(token=request.POST['token']).first().add_time=datetime.datetime.now()
        DBSession.query(Files).filter_by(fileid=request.POST['fileid']).filter_by(token=request.POST['token']).first().md5_hash=file_hash.hexdigest()

    return {"action":"complete","file":request.POST['fileid']}
    
    
    
    
    