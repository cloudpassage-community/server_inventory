import os
import logging
import sys
import lib

# log = logging.getLogger('cphalo-srv_inventory')
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
#     filename="server_inventory.log",
#     filemode='a'
# )

class HaloServerInventory():
    def __init__(self):
        self.halo = lib.ServerController(lib.CONFIG["halo"])
        self.output = [["Server Group", "Server Hostname", "OS Type", "OS Version", "EC2 Instance ID", "Softwares"]]
        self.srv_list = self.halo.get_server()
        self.count = 0
        self.total = len(self.srv_list)

    def run(self):
        for server in self.srv_list:
            tmp = [server["group_name"], server["hostname"], server["platform"], server["platform_version"]]
            if "aws_ec2" in server:
                tmp.append(server["aws_ec2"]["ec2_instance_id"])
            else:
                tmp.append("")
            tmp.extend(self.halo.parse_software_list(self.halo.get_server_software(server["id"])))
            self.write_csv(server["group_name"], [tmp])
            lib.Counter.progress(self.count, self.total)

    def write_csv(self, srv_grp, srv_info):
        encoded_srv_grp = srv_grp.encode('utf-8')
        encoded_srv_info = self.encoding(srv_info)

        filename = "%s.csv" % (encoded_srv_grp)
        if os.path.exists(filename):
            lib.CsvWriter.append(encoded_srv_grp, encoded_srv_info)
        else:
            lib.CsvWriter.write(self.output, encoded_srv_grp, encoded_srv_info)
        self.count += 1

    def encoding(self, data):
        tmp = []
        for i in data:
            tmp.append([x.encode('utf-8') for x in i])
        return tmp

def main():
    halo_inventory = HaloServerInventory()
    # sys.stdout = lib.LoggerWriter(log.info)
    # sys.stderr = lib.LoggerWriter(log.warning)
    sys.stdout.write("Starting to collect server information")
    halo_inventory.run()
    sys.stdout.write("The Script has finished storing all server information")

if __name__ == "__main__":
    main()
