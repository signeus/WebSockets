# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

class RegisterService (IService):
    def __init__(self, core, parameters):
        super(RegisterService, self).__init__(core, parameters)

    def run(self):
        self.core.send(self.parameters["new_client"], {"type":"message", "data":{"comunicacion":"Sockeado!"}})
        return "Register"