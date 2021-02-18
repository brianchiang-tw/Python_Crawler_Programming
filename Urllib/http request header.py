from urllib import request, parse

url = 'http://httpbin.org/post'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host':'httpbin.org',
    'who':'Python Scrapy'
}

dictionary = {
    'name':'Bill',
    'age':30
}

data = bytes(parse.urlencode(dictionary), encoding='utf-8')

req = request.Request(url=url, data=data, headers=headers)

response = request.urlopen(req)

print(response.read().decode('utf-8'))

# str
print( type(response.read().decode('utf-8')) )