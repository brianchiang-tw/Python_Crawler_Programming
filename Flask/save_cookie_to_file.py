import http.cookiejar, urllib.request

filename_1 = 'cookie1.txt'
filenmae_2 = 'cookie2.txt'

# Mozilla format
cookie_1 = http.cookiejar.MozillaCookieJar( filename_1 )

# LWP format
cookie_2 = http.cookiejar.LWPCookieJar( filenmae_2 )

# create handler
handler_1 = urllib.request.HTTPCookieProcessor( cookie_1 )
handler_2 = urllib.request.HTTPCookieProcessor( cookie_2 )

opener_1 = urllib.request.build_opener( handler_1 )
opener_2 = urllib.request.build_opener( handler_2 )

opener_1.open('http://www.baidu.com')
opener_2.open('http://www.baidu.com')

# Save cookie to Mozilla format
cookie_1.save( ignore_discard=True, ignore_expires=True )
cookie_2.save( ignore_discard=True, ignore_expires=True )