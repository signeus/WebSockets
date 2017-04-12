# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

class ReadPostService (IService):
    def __init__(self, core, parameters):
        super(ReadPostService, self).__init__(core, parameters)

    def readDone(self):
        print "Read post: done: "
        self.parameters["data"]["action"] = self.parameters["type"]
        _post_id = self.parameters.get("data", {}).get("id","")
        _user_id = self.parameters.get("data", {}).get("user_id","")
        self.core.FactoryOperation("log", self.parameters.get("data", {}))
        self.core.clients[self.parameters.get("client", {})].get("timers", {}).pop(_post_id, "")


    def run(self):
        #Calculate the time
        _text = self.parameters.get("data", {}).get("post","")
        timeMS = self.core.FactoryOperation("readTime", {"text":_text})
        _post_id = self.parameters.get("data", {}).get("id","")

        #Timers
        timers = self.core.clients[self.parameters.get("client", {})].get("timers", {})
        timers.update({_post_id: self.core.FactoryOperation("activateTimer", {"time": timeMS, "func": self.readDone})})
        self.core.clients[self.parameters.get("client", {})]["timers"] = timers

        self.parameters["data"]["action"] = self.parameters["type"]
        return "Timer activated"