from urllib import request
from urllib.parse import unquote, urlencode
import base64
import json

url = 'http://httpbin.org/post'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host':'httpbin.org',
    'Chinese1':urlencode({'name':'李白'}),
    'MyChinese':base64.b64encode( bytes('中文HTTP請求標頭', encoding='utf-8')),
    'who':'Python Scrapy'
}

dictionary = {
    'name':'Bill',
    'age':30
}

data = bytes(urlencode(dictionary), encoding='utf-8')

req = request.Request(url=url, data=data, headers=headers, method='POST')

req.add_header('Chinese2', urlencode({'國籍':'唐朝'}))

response = request.urlopen(req)

response_value = response.read().decode('utf-8')
print( response_value )

response_json = json.loads(response_value)

print(unquote(response_json['headers']['Chinese1']))
print(unquote(response_json['headers']['Chinese2']))

print(str(base64.b64decode(response_json['headers']['Mychinese'] ),'utf-8') )