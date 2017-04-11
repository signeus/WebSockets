from twisted.python import log
from twisted.internet import reactor
from servers.server import Server
from protocols.protocol import Protocol
import sys

if __name__ == '__main__':
    log.startLogging(sys.stdout)
    ServerFactory = Server
    factory = ServerFactory(u"ws://0.0.0.0:9000")
    factory.protocol = Protocol
    # factory.setProtocolOptions(maxConnections=2)

    # note to self: if using putChild, the child must be bytes...

    reactor.listenTCP(9000, factory)
    reactor.run()
