from twisted.internet import protocol, reactor

host = 'localhost'
port = 9876

class MyProtocol( protocol.Protocol ):

    def sendData( self ):

        data = input('>')

        if data:

            #print(f'...sending {data} to server')
            print('...sending {} to server'.format)
            self.transport.write( data.encode(encoding='utf_8') )
        
        else:
            self.transport.loseConnection()
            

    def connectionMade( self ):
        self.sendData()


    def dataReceived(self, data):

        print( data.decode('utf-8') )
        self.sendData()





class MyFactory( protocol.ClientFactory ):

    protocol = MyProtocol

    clientConnectionLost = lambda self, connector, reason: reactor.stop()
    clientConnectionFailed = clientConnectionLost


reactor.connectTCP( host, port, MyFactory() )

reactor.run()

