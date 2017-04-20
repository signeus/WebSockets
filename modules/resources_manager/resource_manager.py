from resource_factory import ResourceFactory
from modules.configs.environment import env

class ResourceManager:
    def __init__(self, core):
        self.environmentName = env
        self.core = core

    def DatabaseManager(self):
        return self.ManagerOperation(self.environmentName)

    def ResourcesManager(self):
        return self.ManagerOperation(self.environmentName)

    def ManagerOperation(self, environmentName):
        return ResourceFactory(environmentName).config()