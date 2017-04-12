from modules.configs.interfaces.i_enviroment import IEnvironment

class Development(IEnvironment):
    def __init__(self):
        super(Development, self).__init__()
        self.configDict = {
                                'ip_database':'127.0.0.1',
                                'port_database':'27017',
                                'name_database':'kayoo',
                                'name_log_database': 'logKayoo'
                            }

    def config(self):
        return self.configDict