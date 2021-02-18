import requests

from urllib.parse import quote, unquote

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Name':quote('可愛的小貓咪')   
}

r = requests.get('http://httpbin.org/get', headers=headers)

print( type(r.text) )
print( r.text )

response_json = r.json()

print( response_json)

print(f'name { unquote(response_json["headers"]["Name"] ) } ')

