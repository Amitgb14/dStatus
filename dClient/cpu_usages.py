# -*- coding: utf-8 -*-

import os
import psutil

_interval = 1

class CPU:

    def _get_cpu_usages(self):
        cpu_usages = psutil.cpu_percent(interval=_interval, percpu=True)
        return cpu_usages

    def get_cpu(self):
        cpu_usages = self._get_cpu_usages()
        cpu_count = psutil.cpu_count()
        return {'cpu_usages' : cpu_usages,
                'cpu_count' : cpu_count}


if __name__ == '__main__':
    t = CPU()
    v = t.get_cpu()
    print v
