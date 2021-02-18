from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener

from urllib.error import URLError

username = 'bill'
password = '1234'

url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()

p.add_password('localhost', url, username, password)

# create auth handler with http password manager
auth_handler = HTTPBasicAuthHandler(p)

opener = build_opener(auth_handler)

result = opener.open( url )

html = result.read().decode('utf-8')

print( html )