# -*- coding: utf-8 -*-

import ConfigParser
import os

name = 'config/config.cfg'
if not os.path.exists(name):
    raise Exception('Please add a proper cofig file config.cfg')

config = ConfigParser.RawConfigParser()
config.read(name)

HOST = config.get('server', 'host') or '127.0.0.1'
PORT = config.getint('server', 'port') or 9770
DEBUG = config.getboolean('server', 'debug')

CLIENT_PORT = config.getint('client', 'port')
