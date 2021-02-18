from urllib import request, error

import socket

try:
    response = request.urlopen('http://www.jd123.com/test.html')
except error.HTTPError as e:
    print( type(e.reason) )
    print( e.reason, e.code, e.headers )


try:
    response = request.urlopen('https://google.com', timeout=0.01)
except error.HTTPError as e:
    print('error.HTTPError', e.reason)

except error.URLError as e:
    print( type(e.reason) )
    print( 'error.URLError:', e.reason)

    if isinstance(e.reason, socket.timeout):
        print('Time out')
    
    else:
        print('Success')