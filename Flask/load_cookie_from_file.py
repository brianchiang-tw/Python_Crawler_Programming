import http.cookiejar, urllib.request

filename = 'cookies.txt'

cookie = http.cookiejar.LWPCookieJar()

# load cookie from file
cookie.load(filename, ignore_discard=True, ignore_expires=True)

#print( cookie )

handler = urllib.request.HTTPCookieProcessor( cookie )
opener = urllib.request.build_opener( handler )
response = opener.open('http://127.0.0.1:5000/readCookie')

print( response.read().decode('utf-8') )