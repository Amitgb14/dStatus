# -*- coding: utf-8 -*-

import ConfigParser
import os

name = 'dClient/config/config.cfg'
if not os.path.exists(name):
    raise Exception('Please add a proper cofig file config.cfg')

config = ConfigParser.RawConfigParser()
config.read(name)

CLIENT_IP = config.get('client', 'ip')
CLIENT_PORT = config.getint('client', 'port')
