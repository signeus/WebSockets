# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService
from services.database.database_service import DBService

class RegisterService (IService):
    def __init__(self, core, parameters):
        super(RegisterService, self).__init__(core, parameters)

    def run(self):
        return ""