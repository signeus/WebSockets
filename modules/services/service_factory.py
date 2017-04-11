# -*- coding: utf-8 -*-
class ServiceFactory (object):
    def __init__(self, core):
        self.core = core
        self.services = {


        }

    def getTask(self, serviceName, parameters):
        return self.services[serviceName](self.core, parameters)
