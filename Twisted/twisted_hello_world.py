from twisted.internet import reactor

def hello():
    print('Hello World.')


reactor.callWhenRunning(hello)
print('Starting the server')
reactor.run()


# expected output
# Starting the server
# Hello World