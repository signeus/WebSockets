# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService
from modules.utils.timers.timer import Timer

class ActivateTimerService (IService):
    def __init__(self, core, parameters):
        super(ActivateTimerService, self).__init__(core, parameters)

    def run(self):
        _time = self.parameters.get("time",0)
        _func = self.parameters.get("func",None)
        timer = Timer(_time/1000, _func)
        timer.activeTimer()
        return timer