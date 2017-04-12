# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService
from modules.services.database.database_service import DBService
from modules.services.service.logs.collection import collection

class LogService (IService):
    def __init__(self, core, parameters):
        super(LogService, self).__init__(core, parameters)

    def run(self):
        return DBService(self.core).insertIn2Collection(collection, self.parameters)