# -*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE

_command = "df -h"


class Disk:

    def _execute_command(self):
        results = {}
        ps = Popen(_command, stdout=PIPE,
                   stderr=PIPE, shell=True)
        status = ps.wait()
        stdout, stderr = ps.communicate()
        return {'status': status,
                'output': stdout, 'error': stderr
                }

    def calculate_disk(self, data):
        data = data.split("\n")
        # ignore last 'on' word
        # output : ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted']
        header = data[0].split()[:6]
        result = {}
        for disk in data[1:]:
            if disk:
                d = disk.split()
                if d[0].startswith("/d"):
                    disk_report = {
                                    'Filesystem': d[0],
                                    'Size': d[1],
                                    'Used': d[2],
                                    'Available': d[3],
                                    'Use': d[4]}

                    result[d[5]] = disk_report
        return result

    def get_disk(self):
        data = self._execute_command()
        if data['status']:
            return False
        else:
            report = self.calculate_disk(data['output'])
            return report


if __name__ == '__main__':
    t = Disk()
    v = t.get_disk()
    print v
