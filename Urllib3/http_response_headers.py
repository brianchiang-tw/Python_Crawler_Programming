from urllib3 import *

disable_warnings()

http = PoolManager()

url = 'http://www.baidu.com'

response = http.request('GET', url)

response_info = response.info()

for header_key in response_info.keys():
    print(f'header key {header_key} -> {response_info[header_key]}')

    