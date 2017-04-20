# -*- coding: utf-8 -*-
from ldap_connector import LdapConnector

class LdapManager:
	def __init__(self, resourceManagerParameters):
		self.rm = resourceManagerParameters

	def getConnection(self):
		return LdapConnector(self.rm).getConnection()

	def connect2Ldap(self):
		return self.getConnection()
