# -*- coding: utf-8 -*-

#Sockets Management"
from modules.services.service.socket_management.register_service import RegisterService
from modules.services.service.socket_management.unregister_service import UnregisterService

#Actions#
from modules.services.service.actions.connect_service import ConnectService
from modules.services.service.actions.new_post_service import NewPostService
from modules.services.service.actions.read_post_service import ReadPostService

#Logs#
from modules.services.service.logs.log_service import LogService

#Utils#
from modules.services.service.utils.read_time_service import ReadTimeService
from modules.services.service.utils.activate_timer_service import ActivateTimerService
from modules.services.service.utils.deactivate_timer_service import DeactivateTimerService

class ServiceFactory (object):
    def __init__(self, core):
        self.core = core
        self.services = {
            # Sockets Management"
            "register"                  : RegisterService,
            "unregister"                : UnregisterService,
            # Logs#
            "log"                       : LogService,
            # Actions#
            "connect"                   : ConnectService,
            "newPost"                   : NewPostService,
            "readPost"                  : ReadPostService,
            ##Utils##
            "readTime"                  : ReadTimeService,
            "activateTimer"             : ActivateTimerService,
            "deactivateTimer"           : DeactivateTimerService
        }

    def getTask(self, serviceName, parameters):
        return self.services[serviceName](self.core, parameters)
