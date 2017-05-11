# -*- coding: utf-8 -*-
from connectors.mongo_database_connector import MongoDatabaseConnector

class MongoDatabaseManager:
	def __init__(self, resourceManagerParameters):
		self.rm = resourceManagerParameters

	def getConnection(self):
		return MongoDatabaseConnector(self.rm).getConnection()

	def connect2Database(self):
		connection = self.getConnection()
		connection.kayoo.authenticate(self.rm["user_database"], self.rm["psswd_database"], mechanism='SCRAM-SHA-1')
		return connection[self.rm["name_database"]]

	def connect2LogDatabase(self):
		connection = self.getConnection()
		connection.kayooLog.authenticate(self.rm["user_log_database"], self.rm["psswd_log_database"], mechanism='SCRAM-SHA-1')
		return connection[self.rm["name_log_database"]]
