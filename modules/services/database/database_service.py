# -*- coding: utf-8 -*-
from modules.databases.mongo_database_manager import MongoDatabaseManager
from datetime import datetime

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

    def insertDate(self, data):
        try:
            data["date"] = datetime.utcnow()  # .strftime('%Y-%m-%d %H:%M:%S')
            return data
        except Exception, e:
            return "'Date_Created'\n Exception: " + e.message

    def insertIn2Collection(self, collection, data):
        col = self.openLogDBCollection(collection)
        data_completed = self.insertDate(data)
        result = col.insert(data_completed)
        if len(str(result)) <= 0:
            raise Exception("Error inserting")
        data_completed["_id"] = str(result)
        data_completed["date"] = int(data_completed["date"].strftime("%s"))
        return data_completed