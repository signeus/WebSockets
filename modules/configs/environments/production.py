import socket
from modules.configs.interfaces.i_enviroment import IEnvironment

class Production(IEnvironment):
    def __init__(self):
        super(Production, self).__init__()
        externalIp = str([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
        self.configDict = {
                                'ip_database':'database',
                                'port_database':'27017',
                                'name_database':'kayoo',
                                'name_log_database': 'log_kayoo',
                                'ip_app': externalIp
                            }

    def config(self):
        return self.configDict