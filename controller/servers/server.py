from autobahn.twisted.websocket import WebSocketServerFactory
from modules.core.core import Core
from modules.services.service_factory import ServiceFactory
from modules.resources_manager.resource_manager import ResourceManager

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
            print "------> " + ex + " Type: " + type(ex) + " <------"
            return {"result": 1, "data": {"message": ex.message, "error": 1, "type": 1}}

    def GetDatabaseResources(self):
        try:
            return self.rm.DatabaseManager()
        except Exception, ex:
            return ex.message

    ##End CORE##

    def register(self, client):
        if client.peer not in self.clients:
            self.clients[client.peer] = {"client": client}
            result = self.FactoryOperation("register", {"clients":self.clients, "new_client":client.peer})
            print "Registed client: {}".format(client.peer)
            print result

    def unregister(self, client):
        if client.peer in self.clients:
            self.clients.pop(client.peer)
            result = self.FactoryOperation("unregister", {"clients":self.clients, "pop_client":client.peer})
            print "Unregisted client: {}".format(client.peer)
            print result

    def process_message(self, client, msg):
        try:

            #m = json.loads(msg)
            m = msg
            if m["type"] == "connect":
                return ""
                # col.insert({"event": m["type"], "user_id": m["user"], "ts": datetime.datetime.now()})
                # self.clients[client.peer]["user"] = {"id": m["user"]}
                # print self.find_client(m["user"])
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