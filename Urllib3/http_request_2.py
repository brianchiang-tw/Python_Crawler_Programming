from urllib3 import *
from urllib.parse import urlencode

disable_warnings()

http = PoolManager()

url = 'http://www.baidu.com/s'

print(url)

response = http.request('GET', url, fields = {'wd':'cat'})
data = response.data.decode('utf-8')

print( data )