# -*- coding: utf-8 -*-

import socket
from memory_usages import Memory
from disk_usages import Disk
from cpu_usages import CPU

_machine_name = socket.gethostname()


# Get Mepmory
def get_memory():
    m = Memory()
    return m.get_memory()


# Get Disk
def get_disk():
    d = Disk()
    return d.get_disk()


def get_cpu():
    c = CPU()
    return c.get_cpu()


def main():
    report = {_machine_name:
              {
               'memory': get_memory(),
               'disk': get_disk(),
               'cpu': get_cpu(),
              }}
    return report
