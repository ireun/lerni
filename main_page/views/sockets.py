# -*- coding: utf-8 -*-
from base import *
import psutil
from pyramid.security import authenticated_userid
import datetime
import json

from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from socketio.mixins import BroadcastMixin
import gevent
import random


class NamedUsersRoomsMixin(BroadcastMixin):
    def __init__(self, *args, **kwargs):
        super(NamedUsersRoomsMixin, self).__init__(*args, **kwargs)
        if 'rooms' not in self.session:
            self.session['rooms'] = set()  # a set of simple strings
        if 'username' not in self.session:
            self.session['username'] = ""

    def join(self, room):
        """Lets a user join a room on a specific Namespace."""
        self.session['rooms'].add(self._get_room_name(room))

    def leave(self, room):
        """Lets a user leave a room on a specific Namespace."""
        self.session['rooms'].remove(self._get_room_name(room))

    def _get_room_name(self, room):
        return self.ns_name + '_' + room

    def emit_to_room(self, room, event, *args):
        """This is sent to all in the room (in this particular Namespace)"""
        pkt = dict(type="event",
                   name=event,
                   args=args,
                   endpoint=self.ns_name)
        room_name = self._get_room_name(room)
        for sessid, socket in self.socket.server.sockets.iteritems():
            if 'rooms' not in socket.session:
                continue
            if room_name in socket.session['rooms'] and self.socket != socket:
                socket.send_packet(pkt)

    def get_room_members(self, room):
        members = []
        room_name = self._get_room_name(room)
        for sessid, socket in self.socket.server.sockets.iteritems():
            if 'rooms' not in socket.session:
                continue
            if room_name in socket.session['rooms']:
                members.append({'type': 'grey', 'nick': socket.session['username']})
        return members

    def check_username_avaibility(self, username):
        for sessid, socket in self.socket.server.sockets.iteritems():
            if 'rooms' not in socket.session:
                continue
            if self.socket != socket and socket.session['username'] == username:
                return False
        return True


class ChatNamespace(BaseNamespace, NamedUsersRoomsMixin):
    def initialize(self):
        self.session['username'] = ""

    def on_chat(self, msg):
        if msg[0] == "/":
            command = msg.split(" ")
            if command[0] == "/nick" and len(command) == 2:
                self.on_set_username(command[1])
            elif command[0] == "/refresh" and command[1] == "users":
                self.emit("userlist", self.get_room_members("main"))
            else:
                pass
        elif self.session['username']:
            self.emit_to_room("main", "message", {"us": self.session['username']+": ", "text": msg})
        else:
            self.emit("message", {
                "type": "host", "us": "Serwer", "text": u"Aby brać udział w dyskusji musisz najpierw wybrać swój nick"})

    def on_set_username(self, msg):
        if self.check_username_avaibility(msg):
            self.session['username'] = msg
            self.emit("set_username", msg)
        else:
            self.emit("chat_alert", "Wybrany pseudonim jest już zajęty.")

    def recv_connect(self):
        self.broadcast_event('user_connect')
        self.emit("set_username", "")
        print "USER CONN"

    def recv_disconnect(self):
        self.broadcast_event('user_disconnect')
        self.disconnect(silent=False)

    def on_join(self, channel):
        self.join(channel)
        self.emit_to_room(channel, "message", { "type": "host", "us": "Serwer", "text": u"*** Użytkownik "+
                                                self.session['username'] + u" dołączył do kanału ***" })
        self.emit("message", {"type": "host", "us": "Serwer", "text": u"*** Połączono z chatem. ***"})
        user_list = self.get_room_members(channel)
        self.emit_to_room(channel, "userlist", user_list)
        self.emit("userlist", user_list)

#class StatNamespace(BaseNamespace, NamedUsersRoomsMixin):
#    def initialize(self):
#        print "INIT"
#        self.join("main")
#        self.emit("sine", {'value': 123})
#        #self.spawn(self.job_chat)

#    def on_boo(self, data):
#        print "BOO", data
#        self.emit("Boo")

    #def job_chat(self):
    #    import time
    #    cnt = 0
    #    while True:
    #        cnt += 1
    #        tm = time.time()
    #        self.emit("message", {"us": "Kamil Danak", "text": tm*1000})
    #        gevent.sleep(2)
    #    pass

@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ,
                    {"/chat": ChatNamespace},
                    request=request)
    return Response('')

