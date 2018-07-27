# -*- coding: utf-8 -*-
import csv

class CsvWriter(object):
    @staticmethod
    def write(output, server_group, srvs_info):
        filename = "%s.csv" % server_group
        with open(filename, "wb") as f:
            writer = csv.writer(f.encode('utf-8'))
            writer.writerows(output.encode('utf-8'))
            writer.writerows(srvs_info.encode('utf-8'))

    @staticmethod
    def append(server_group, srvs_info):
        filename = "%s.csv" %server_group
        with open(filename, "a") as f:
            writer = csv.writer(f.encode('utf-8'))
            try:
                writer.writerows(srvs_info)
            except UnicodeError:
                srvs_info = srvs_info.encode('utf-8')