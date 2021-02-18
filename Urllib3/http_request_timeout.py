from os import read
from urllib3 import *
disable_warnings()


http = PoolManager( timeout=Timeout(connect=2.0, read=2.0) )

url1 = 'https://www.dummyweb.org'
url2 = 'https://httpbin.org/delay/3'


try:
    http.request('GET', url1, timeout=Timeout(connect=2.0, read=4.0) )

except Exception as e:
    print(f'error occur: {e}')

print('\n\n\n')

response = http.request('GET', url2, timeout=Timeout(connect=2.0, read=4.0) )

print('---------------')

print( response.info() )

print('---------------')

print( response.info()['Content-Length'] )


print('---------------')
# time out due to 3 seconds delay
response = http.request('GET', url2, timeout=Timeout(connect=2.0, read=2.0) )