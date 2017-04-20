# -*- coding: utf-8 -*-
import ldap
import ldap.functions as lf

class LdapConnector:
    def __init__(self, resourceManagerParameters):
        self.server = resourceManagerParameters["server_ldap"]
        self.baseDN = resourceManagerParameters["baseDN_ldap"]
        self.user = resourceManagerParameters["user_ldap"]
        self.password = resourceManagerParameters["password_ldap"]

    def getConnection(self):
        lf.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        connect = lf.initialize(self.server)
        connect.simple_bind_s(self.user, self.password)
        return connect
