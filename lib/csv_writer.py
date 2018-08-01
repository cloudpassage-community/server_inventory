# -*- coding: utf-8 -*-
import csv

class CsvWriter(object):
    @staticmethod
    def write(output, server_group, srvs_info):
        filename = "%s.csv" % server_group
        encoded_filename = filename.encode('utf-8')
        with open(encoded_filename, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(output.encode('utf-8'))
            writer.writerows(srvs_info.encode('utf-8'))

    @staticmethod
    def append(server_group, srvs_info):
        filename = "%s.csv" %server_group
        encoded_filename = filename.encode('utf-8')
        with open(encoded_filename, "a") as f:
            writer = csv.writer(f)
            try:
                writer.writerows(srvs_info)
            except UnicodeError:
                srvs_info = srvs_info.encode('utf-8')