# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

class DeactivateTimerService (IService):
    def __init__(self, core, parameters):
        super(DeactivateTimerService, self).__init__(core, parameters)

    def run(self):
        _post_id = self.parameters.get("post_id","")
        if not _post_id:
            return "Doesn't have post"

        _t = self.core.clients[self.parameters.get("client", {})].get("timers", {}).pop(_post_id, "")
        _t.timer.deactivateTimer()
