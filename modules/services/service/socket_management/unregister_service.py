# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

class UnregisterService (IService):
    def __init__(self, core, parameters):
        super(UnregisterService, self).__init__(core, parameters)

    def run(self):
        return "Unregister"