# -*- coding: utf-8 -*-
from base import *
import os
import re
import hashlib
import random
import time

upload_path = "main_page/uploads/"
packet_size = 512*512


@view_config(route_name='file_upload', renderer='jsonp', request_param=['totalSize', 'type', 'fileName', 'totalSize'])
def new_upload(request):
    file_data = str(request.POST['totalSize']) + "|" + re.sub('/[^A-Za-z0-9/]/', '', request.POST['type']) +\
        "|" + re.sub('/[^A-Za-z0-9/]/', '', request.POST['fileName'])
    original_file_name = request.POST['fileName']
    token = hashlib.md5(file_data).hexdigest()
    fileid = str(time.time())+str(random.randint(5, pow(2, 31) - 1))
    while DBSession.query(Files).filter_by(fileid=fileid).count() != 0:
        fileid = str(time.time())+str(random.randint(5, pow(2, 31) - 1))
    with transaction.manager:
        DBSession.add_all([Files(file_data, fileid, token, original_file_name, "", datetime.datetime.now())])
    return {"action": "new_upload", "fileid": fileid, "token": token}


@view_config(route_name='file_upload', renderer='jsonp', request_param=['fileid', 'token', 'packet'])
def get_packet(request):
    fileid = request.POST['fileid']
    token = request.POST['token']
    if DBSession.query(Files).filter_by(fileid=fileid).filter_by(token=token).count() != 0:
        filename = request.GET['fileid']+"-"+request.GET['packet']
        input_file = request.POST['data'].file
        file_path = upload_path+filename
        temp_file_path = file_path + '~'
        output_file = open(temp_file_path, 'wb')
        input_file.seek(0)
        while True:
            data = input_file.read(2 << 16)
            if not data:
                break
            output_file.write(data)
        output_file.close()
        os.rename(temp_file_path, file_path)
        return {"action": "new_packet", "result": "success", "packet": request.GET['packet']}
    ## Return no such file error


@view_config(route_name='file_upload', renderer='jsonp', request_param=['fileid', 'token'])
def merge_files(request):
    fileid = request.POST['fileid']
    token = request.POST['token']
    if DBSession.query(Files).filter_by(fileid=fileid).filter_by(token=token).count() == 0:
        return {"error": "No file found in the database for the provided ID / token"}
    else:
        f = DBSession.query(Files).filter_by(fileid=fileid).filter_by(token=token).first()
    if not f.uploaded:
        file_data_list = f.fileData.split("|")
        file_size = file_data_list[0]
        #file_type = file_data_list[1]
        #file_name = file_data_list[2]

        total_packages = ceil(float(file_size)/packet_size)
        for package in range(int(total_packages)):
            try:
                with open(upload_path+request.POST['fileid']+"-"+str(package)):
                    pass
            except IOError:
                return {"error": "Missing package #"+str(package)}
        try:
            output_file = open(upload_path+request.POST['fileid'], 'ab')
        except IOError:
            return {"error": "Unable to create new file for merging"}

        file_hash = hashlib.md5()
        for package in range(int(total_packages)):
            input_file = open(upload_path+fileid+"-"+str(package), 'rb')
            input_data = input_file.read()
            output_file.write(input_data)
            file_hash.update(input_data)
            input_file.close()
            os.remove(upload_path+fileid+"-"+str(package))
        output_file.close()
        f.add_time = datetime.datetime.now()
        f.md5_hash = file_hash.hexdigest()
        f.uploaded = True
    return {"action": "complete", "file": request.POST['fileid']}