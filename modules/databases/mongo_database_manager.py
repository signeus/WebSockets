# -*- coding: utf-8 -*-
from connectors.mongo_database_connector import MongoDatabaseConnector

class MongoDatabaseManager:
	def __init__(self, resourceManagerParameters):
		self.rm = resourceManagerParameters

	def getConnection(self):
		return MongoDatabaseConnector(self.rm).getConnection()

	def connect2Database(self):
		return self.getConnection()[self.rm["name_database"]]

	def connect2LogDatabase(self):
		return self.getConnection()[self.rm["name_log_database"]]
