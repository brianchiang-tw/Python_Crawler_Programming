from urllib3 import *
from urllib.parse import urlencode

disable_warnings()

http = PoolManager()

url = 'http://www.baidu.com/s?' + urlencode({'wd':'Cat'})

print(url)

response = http.request('GET', url)
data = response.data.decode('utf-8')

print( data )