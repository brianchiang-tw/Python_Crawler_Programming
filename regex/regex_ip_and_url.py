import re

pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ipaddr = '168.95.192.1'

result = re.findall(pattern, ipaddr)
# ['168.95.192.1']
print( result )


pattern = 'https?:/{2}\w.+'
url = 'https://www.google.com'

result = re.findall(pattern, url)
# ['https://www.google.com']
print( result )

url = 'http://www.google.com'
result = re.findall(pattern, url)
# ['http://www.google.com]
print( result )

url = 'ftp://www.google.com'
result = re.findall(pattern, url)
# [] (Empty, no match)
print( result )