import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
}

response = requests.get('https://www.google.com', headers=headers)

print('\n\n\n')
# status code
print( type(response.status_code) )
print( response.status_code )

print('\n\n\n')
# response header
print( type(response.headers) )
print( response.headers )


print('\n\n\n')
# response header
print( type(response.cookies) )
print( response.cookies )



print('\n\n\n')
# response header
print( type(response.url) )
print( response.url )



print('\n\n\n')
# status code
if response.status_code == requests.codes.ok:
    print('ok')

else:
    print('failed')