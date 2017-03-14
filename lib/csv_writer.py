import csv

class CsvWriter(object):
    @staticmethod
    def write(output, server_group, srvs_info):
    	filename = "%s.csv" % server_group
        with open(filename, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(output)
            writer.writerows(srvs_info)