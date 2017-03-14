import lib
from collections import defaultdict

class HaloServerInventory():
    def __init__(self):
        self.halo = lib.ServerController(lib.CONFIG["halo"])
        self.output = [["Server Group", "Server Hostname", "OS Type", "OS Version", "EC2 Instance ID", "Softwares"]]
        self.dict = defaultdict(list)

    def build(self):
        for server in self.halo.get_server():
            tmp = [server["group_name"], server["hostname"], server["platform"], server["platform_version"]]
            if "aws_ec2" in server:
                tmp.append(server["aws_ec2"]["ec2_instance_id"])
            else:
                tmp.append("")
            tmp.append(self.halo.parse_software_list(self.halo.get_server_software(server["id"])))
            self.dict[server["group_name"]].append(tmp)

    def run(self):
        self.build()
        for server_group in self.dict:
            lib.CsvWriter.write(self.output, server_group, self.dict[server_group])

def main():
    halo_inventory = HaloServerInventory()
    halo_inventory.run()

if __name__ == "__main__":
    main()
