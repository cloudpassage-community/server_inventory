import os
import lib

class HaloServerInventory():
    def __init__(self):
        self.halo = lib.ServerController(lib.CONFIG["halo"])
        self.output = [["Server Group", "Server Hostname", "OS Type", "OS Version", "EC2 Instance ID", "Softwares"]]

    def run(self):
        for server in self.halo.get_server():
            tmp = [server["group_name"], server["hostname"], server["platform"], server["platform_version"]]
            if "aws_ec2" in server:
                tmp.append(server["aws_ec2"]["ec2_instance_id"])
            else:
                tmp.append("")
            tmp.append(self.halo.parse_software_list(self.halo.get_server_software(server["id"])))
            self.write_csv(server["group_name"], [tmp])

    def write_csv(self, srv_grp, srv_info):
        filename = "%s.csv" %srv_grp
        if os.path.exists(filename):
            lib.CsvWriter.append(srv_grp, srv_info)
        else:
            lib.CsvWriter.write(self.output, srv_grp, srv_info)

def main():
    halo_inventory = HaloServerInventory()
    halo_inventory.run()

if __name__ == "__main__":
    main()
