# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

class NewCommunityService (IService):
    def __init__(self, core, parameters):
        super(NewCommunityService, self).__init__(core, parameters)

    def run(self):
        self.parameters["data"]["action"] = self.parameters["type"]
        return self.core.FactoryOperation("log",self.parameters.get("data",{}))