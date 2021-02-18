import urllib.request

# transform dictionary into string
payload = urllib.parse.urlencode({'name':'Bill','age':30})

# transform payload to raw bytes, encoding in utf-8
data = bytes(payload, encoding='utf-8')

# HTTP POST action
response = urllib.request.urlopen('http://httpbin.org/post', data=data)

# HTTP POST action result
result = response.read().decode('utf-8')

print(result)
