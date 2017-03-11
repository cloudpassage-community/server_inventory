import math
import cloudpassage


class ServerController(object):
    def __init__(self, config):
        session = cloudpassage.HaloSession(config["api_key"],
                                           config["api_secret_key"])
        self.server_obj = cloudpassage.Server(session)
        self.request_obj = cloudpassage.HttpHelper(session)

    def get_server(self):
        return self.server_obj.list_all()

    def get_srv_software_pag(self, count, srv_id):
        result = []
        iteration = int(math.ceil(count / 100.0)) + 1
        for page in range(2, iteration):
            endpoint = "/v2/servers?id=%s&group_by=package_name,package_version&per_page=100&page=%s&sort_by=package_name.asc" % (srv_id, page)
            softwares = self.request_obj.get(endpoint)
            result.extend(softwares["servers"])
        return result

    def get_server_software(self, srv_id):
        result = []
        endpoint = "/v2/servers?id=%s&group_by=package_name,package_version&per_page=100&page=1&sort_by=package_name.asc" % (srv_id)
        softwares = self.request_obj.get(endpoint)
        result.extend(softwares["servers"])
        if softwares["count"] > 100:
            result.extend(self.get_srv_software_pag(softwares["count"], srv_id))
        return result


    def parse_software_list(self, softwares):
        sw_name = ""
        for software in softwares:
            sw_name += "%s (%s), " % (software["package_name"], software["package_version"])
        return sw_name