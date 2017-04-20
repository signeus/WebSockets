class Caller():
    def __init__(self, serviceFactory, serviceName, parameters):
        self.serviceFactory = serviceFactory
        self.serviceName = serviceName
        self.parameters = parameters

    def firstCall(self):
        try:
            serviceResult = self.serviceFactory.getTask(self.serviceName, self.parameters).run()
            return {"data": serviceResult, "result": 0, "type":self.serviceName}
        except Exception, ex:
            print "------> "
            print "Service: "
            print self.serviceName
            print ex
            print "Type: "
            print type(ex)
            print "<------"
            return {"result": 1, "data": {"message": ex.message, "error": 1, "type": 1}}

    def call(self):
        try:
            serviceResult = self.serviceFactory.getTask(self.serviceName, self.parameters).run()
            return serviceResult
        except Exception, ex:
            print "------> "
            print "Service: "
            print self.serviceName
            print ex
            print "Type: "
            print type(ex)
            print "<------"