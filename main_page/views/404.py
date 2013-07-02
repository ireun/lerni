# -*- coding: utf-8 -*-
from base import *
#@notfound_view_config(renderer='main.mak')
#def notfound(request):
#    logged_in = authenticated_userid(request)
#    try:
#       menu_top_list =[]
#       for position in DBSession.query(MenuTop):
#       	menu_top_list.append([position.link,position.name])
#       menu_left_list =[]
#       for position in DBSession.query(MenuLeft):
#       	menu_left_list.append([position.link,position.name])
#       current_datetime=str(datetime.datetime.now())
#       articles = [[0,"404 Not Found",current_datetime[:current_datetime.find(".")],"The Page",'<img src="/static/404.jpg"></img>',0]]
#    except DBAPIError:
#        return Response(conn_err_msg, content_type='text/plain', status_int=500)
#    return {'menu_top_list':menu_top_list, 'menu_left_list':menu_left_list, 'articles':articles, 'logged_in':logged_in}
#    return Response('Not found, dude!', status='404 Not Found')
