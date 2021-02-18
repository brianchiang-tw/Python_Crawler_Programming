import urllib.request

url = 'https://baidu.com'
response = urllib.request.urlopen( url )
content = response.read().decode('utf-8')
#print(content) 

print( type(response) )