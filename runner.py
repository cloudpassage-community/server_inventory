import lib

class HaloServerInventory():
    def __init__(self):
        self.halo = lib.ServerController(lib.CONFIG["halo"])
        self.output = [["Server Group", "Server Hostname", "OS Type", "OS Version", "EC2 Instance ID", "Softwares"]]

    def build(self):
        for server in self.halo.get_server():
            tmp = [server["group_name"], server["hostname"], server["platform"], server["platform_version"]]
            if "aws_ec2" in server:
                tmp.append(server["aws_ec2"]["ec2_instance_id"])
            else:
                tmp.append("")
            tmp.append(self.halo.parse_software_list(self.halo.get_server_software(server["id"])))
            self.output.append(tmp)

    def run(self):
        self.build()
        lib.CsvWriter.write(self.output)

def main():
    halo_inventory = HaloServerInventory()
    halo_inventory.run()

if __name__ == "__main__":
    main()
