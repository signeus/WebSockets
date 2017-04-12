from autobahn.twisted.websocket import WebSocketServerFactory
from modules.services.service_factory import ServiceFactory
from modules.resources_manager.resource_manager import ResourceManager
from django.utils.encoding import smart_str
import json

class Server(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.serviceFactory = ServiceFactory(self)
        self.rm = ResourceManager(self)
        self.clients = {}

    ##CORE##

    def FactoryOperation(self, serviceName, parameters, internalContext=False):
        try:
            serviceResult = self.serviceFactory.getTask(serviceName, parameters).run()
            if not internalContext:
                return {"data": serviceResult, "result": 0}

            return serviceResult
        except Exception, ex:
            print "------> "
            print ex
            print "Type: "
            print type(ex)
            print "<------"

            return {"result": 1, "data": {"message": ex.message, "error": 1, "type": 1}}

    def GetDatabaseResources(self):
        try:
            return self.rm.DatabaseManager()
        except Exception, ex:
            return ex.message

    def GetClient(self, peer):
        return self.clients[peer]

    ##End CORE##

    def register(self, client):
        if client.peer not in self.clients:
            self.clients[client.peer] = {"client": client}
            result = self.FactoryOperation("register", {"new_client":client})
            print result
            print "Registed client: {}".format(client.peer)

    def unregister(self, client):
        if client.peer in self.clients:
            self.clients.pop(client.peer)
            result = self.FactoryOperation("unregister", {"removed_client":client})
            print result
            print "Unregisted client: {}".format(client.peer)

    def process_message(self, client, msg):
        try:
            message = json.loads(msg)
            print message
            message.get("data",{})["client"] = client.peer
            result = self.FactoryOperation(message.get("type"," "), message)
            print result
                # self.send(self.clients[client.peer]["client"], {"type": "message", "data": {"mesage": "hola"}})
        except Exception, ex:
            print "Websocket server error"
            print ex
            pass

    def send(self, client, message):
        client.sendMessage(json.dumps(message))

    def broadcast(self, msg):

        for k, v in self.clients.iteritems():
            self.send(v["client"], {"type": "message", "data": {"message": "hello"}})

    def find_client(self, client_id):
        for k, v in self.clients.iteritems():
            if "user" in v:
                if v["user"]["id"] == client_id:
                    return v
        return {}