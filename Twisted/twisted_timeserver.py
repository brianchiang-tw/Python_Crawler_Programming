from twisted.internet import protocol, reactor

from time import ctime

port = 9876

class MyProtocol( protocol.Protocol ):

    def connectionMade( self ):

        client = self.transport.getPeer().host

        print(f'Client {client} has connected to server')

    
    def dataReceived( self, data ):

        self.transport.write( ctime().encode( encoding='utf-8' ) + b' ' + data )
    

factory = protocol.Factory()

factory.protocol = MyProtocol

print('Waiting for client')

# listen to specif port and new connection
reactor.listenTCP(port, factory )

reactor.run()

