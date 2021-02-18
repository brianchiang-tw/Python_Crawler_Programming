import requests

r = requests.get('http://www.taobao.com')

print('type of response', type(r) )

print('status code', r.status_code )

print('type of response text', type(r.text) )

print('\n\n\n')

print('cookie of response', r.cookies )

print('\n\n\n')

#print('response text', r.text)