import urllib.request

url = 'https://www.jd.com'

response = urllib.request.urlopen(url)

print(f'Type of response: { type(response) }')

print(f'Status: { response.status }')

print(f'Message: { response.msg }')

print(f'Version: { response.version }')

print(f'Header: { response.getheaders() } ' )