# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService
from modules.ldap.ldap_manager import LdapManager

class LdapConnectService (IService):
    def __init__(self, core, parameters):
        super(LdapConnectService, self).__init__(core, parameters)

    def run(self):
        return LdapManager(self.core.GetResources()).connect2Ldap()