# -*- coding: utf-8 -*-

import os
import time

_filename = "/proc/meminfo"


class Memory:

    def __init__(self):
        self.memory_file = _filename

    def scan_memory(self):
        if os.path.isfile(self.memory_file):
            with open(self.memory_file) as fread:
                self.calculate_memory(fread.readlines()[:3])

    def calculate_memory(self, data):
        self.total_memory = float(data[0].split()[1])
        self.available_memory = float(data[2].split()[1])
        self.usages_memory = self.total_memory-self.available_memory
        self.free_memory = self.total_memory-self.usages_memory

    def get_memory(self):
        self.scan_memory()
        data = {}
        data['total_memory'] = round(self.total_memory/(1024*1024), 2)
        data['free_memory'] = round(self.free_memory/(1024*1024), 2)
        data['usages_memory'] = round(self.usages_memory/(1024*1024), 2)
        mem_per = (self.usages_memory/self.total_memory)*100
        data['memory_percentage'] = round(mem_per, 2)
        return data


if __name__ == '__main__':
    t = Memory()
    v = t.get_memory()
