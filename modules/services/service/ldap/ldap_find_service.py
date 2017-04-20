# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

import ldap

class LdapFindService (IService):
    def __init__(self, core, parameters):
        super(LdapFindService, self).__init__(core, parameters)

    def run(self):
        search = self.parameters.get("search", '')
        searchScope = ldap.SCOPE_SUBTREE
        #searchFilter = "uid=*kevin.m*"
        searchFilter = 'cn=*' +search+'*'
        connection = self.core.FactoryOperation("connectLDAP", {})
        baseDN = self.core.GetResources()["baseDN_ldap"]
        ldap_result_id = connection.search(baseDN, searchScope, searchFilter)

        result_set = []
        while 1:
            result_type, result_data = connection.result(ldap_result_id, 0)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
        return result_set