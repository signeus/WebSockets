# -*- coding: utf-8 -*-
from modules.services.interfaces.i_service import IService

class ReadTimeService (IService):
    def __init__(self, core, parameters):
        super(ReadTimeService, self).__init__(core, parameters)

    def run(self):
        _text = self.parameters.get("text","")

        if not _text:
            return 0.0

        milliSeconds = 0.0
        for i in _text:
            if i == "." or i == ",":
                milliSeconds = milliSeconds + 2.0
                continue
            if i == " ":
                continue
            milliSeconds = milliSeconds + 8.0
        return milliSeconds