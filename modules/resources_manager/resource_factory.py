from modules.configs.environments.development import Development
from modules.configs.environments.production import Production

class ResourceFactory (object):
    def __new__(cls, environmentName):
        resources = {
                        "development" : Development,
                        "production": Production
                    }
        return resources[environmentName]()