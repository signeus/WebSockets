# -*- coding: utf-8 -*-
from databases.mongo_database_manager import MongoDatabaseManager
class DBService:
    def __init__(self, core):
        self.core = core

    def openDB(self):
        return MongoDatabaseManager(self.core.GetDatabaseResources())

    def openLogDBCollection(self, collection):
        db = self.openDB().connect2LogDatabase()
        return db[collection]

    def openDBCollection(self, collection):
        db = self.openDB().connect2Database()
        return db[collection]
