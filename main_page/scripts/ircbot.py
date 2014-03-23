# -*- coding: utf-8 -*-
import os
import sys
import transaction
import datetime
from sqlalchemy import engine_from_config
import random

from os import listdir
from os.path import isfile, join
import codecs

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import (
    DBSession,
    LuckyNumbers)

import logging
from contextlib import closing
import socket
import argparse
import select
from textwrap import wrap
import subprocess
import irclib
from time import sleep
from main_page.views.base import get_week, setting_save, setting_load


class Socket(object):
    __slots__ = ("socket", "on_read", "on_write", "sockets")

    def __init__(self, sock, on_read=None, on_write=None):
        self.socket = sock
        if on_read:
            self.on_read = on_read
        if on_write:
            self.on_write = on_write


class Network(object):
    __slots__ = ('sockets', 'filenos')

    def __init__(self):
        self.sockets = []
        self.filenos = {}

    def listen(self, addr, port, on_read):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.add_socket(sock, lambda s: self.accept(s, on_read))
        sock.bind((addr, port))
        sock.listen(1)

    def accept(self, sock, on_read):
        logging.debug("Accepting a connection")
        conn, _ = sock.accept()
        self.add_socket(conn, on_read)

    def add_socket(self, sock, on_read=None, on_write=None):
        logging.debug("Adding socket %d", sock.fileno())
        self.sockets.append(sock)
        self.filenos[sock.fileno()] = Socket(sock, on_read, on_write)

    def remove_socket(self, sock):
        logging.debug("Removing socket %d", sock.fileno())
        self.sockets.remove(sock)
        del self.filenos[sock.fileno()]

    def run_forever(self):
        while True:
            logging.debug("Entering select...")
            (can_read, _, _) = select.select(self.sockets, [], [])
            [self.filenos[sock.fileno()].on_read(sock) for sock in can_read]


class IRCBot:
    def __init__(self, server, chan, key, nickname, password, local_port):
        self.network = Network()
        self.chan = chan
        self.nickname = nickname
        self.password = password
        self.key = key
        self.ircobj = irclib.IRC(self.add_socket, self.rm_socket)
        self.connection = self.ircobj.server()
        self.ircobj.add_global_handler("all_events", self._dispatcher, -10)
        self.ircobj.add_global_handler("welcome", self.on_connect)
        self.ircobj.add_global_handler("nicknameinuse", self.on_nicknameinuse)
        self.connection.connect(server, 6667, nickname)
        self.network.listen("127.0.0.1", local_port, self.read_message)
        self.network.run_forever()


    def on_nicknameinuse(self, c, _):
        c.nick(c.get_nickname() + "_")

    def on_connect(self, connection, _):
        connection.join(self.chan, self.key)

    def read_message(self, sock):
        """
        Read a message on the local socket and write it to the channel
        """
        data = sock.recv(1024)
        if not data:
            self.network.remove_socket(sock)
        else:
            self.privmsg(self.chan, data)

    def privmsg(self, to, message):
        """
        Write a message to the channel
        """
        if len(message) > 0:
            for line in message.split('\n'):
                wrapped = wrap(line, 512 - len("\r\n") -
                                     len("PRIVMSG %s :" % self.chan))
                for wrapped_line in wrapped:
                    if len(wrapped_line.strip()) > 0:
                        self.connection.privmsg(to, wrapped_line)
                        sleep(1)

    def add_socket(self, sock):
        self.network.add_socket(sock, lambda s: self.ircobj.process_data([s]))

    def rm_socket(self, sock):
        self.network.remove_socket(sock)

    @staticmethod
    def event_info(event):
        source = event.source().split('!', 1) \
            if event.source() is not None else []
        s_login = source[0] if len(source) > 0 else ""
        s_host = source[1] if len(source) > 1 else ""
        target = event.target().split('!', 1) \
            if event.target() is not None else []
        t_login = target[0] if len(target) > 0 else ""
        t_host = target[1] if len(target) > 1 else ""
        return event.eventtype(), s_login, s_host, t_login, t_host

    def _dispatcher(self, _, event):
        etype, s_login, s_host, t_login, t_host = IRCBot.event_info(event)
        if "lucky" in event.arguments():
            print event.arguments()
            message = "Szczęśliwe numerki na ten tydzien to: "
            week = get_week(datetime.datetime.now().date() + datetime.timedelta(1))
            for x in DBSession.query(LuckyNumbers).filter(LuckyNumbers.date.between(week[0], week[1])):
                message += str(x.number) + ", "
            message = message[:-2] + "."
            self.privmsg("#staszic", message)

        if len(event.arguments()) > 0 and "random" in event.arguments()[0].split(" "):
            arg = event.arguments()[0].split(" ")
            self.privmsg("#staszic", "Wylosowalem " + str(random.randint(int(arg[1]), int(arg[2]))))

        if len(event.arguments()) > 0 and event.arguments()[0].find('zmieniony') != -1:
            self.privmsg("NickServ", "IDENTIFY " + self.password)

        if etype == "namreply":
            setting_save("irc_users", str(len(event.arguments()[2].strip().split(" "))))
        if etype == "quit":
            self.connection.send_raw("NAMES #staszic")

        if etype == "join" and self.nickname != s_login:
            self.privmsg("#staszic", "Witaj na kanale IV Liceum Ogólnokształcącego w Sosnowcu! Pytania, opinie, "
                                     "komentarze? Kandydat? Z chęcią pomożemy! Zdarza się, że nikogo na kanale nie ma "
                                     "- wtedy poczekaj jakiś czas lub napisz pytanie na adres staszic1@staszic.edu.pl")
            self.connection.send_raw("NAMES #staszic")

        if etype == "ping":
            self.connection.send_raw("NAMES #staszic")
            #privmsg #privnotice


def netwrite(to_send, host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.connect((host, port))
        [sock.send(data) for data in to_send]


def say_something(conf):
    if len(conf.message) == 1 and conf.message[0] == '-':
        netwrite(sys.stdin, '127.0.0.1', conf.local_port)
    else:
        netwrite([' '.join(conf.message)], '127.0.0.1', conf.local_port)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """

    :param argv:
    """
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    #Base.metadata.create_all(engine)
    IRCBot(setting_load("irc_host"), setting_load("irc_channel"), "",
           setting_load("irc_login"), setting_load("irc_password"), 6668)




