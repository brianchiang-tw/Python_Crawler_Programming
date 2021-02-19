from requests import Request, Session

url = 'https://httpbin.org/post'

data = {
    'name': 'Cute Cat',
    'age' : 5
}

headers = {
    'country' : 'USA'
}

session = Session()

req = Request('post', url, data=data, headers=headers)

packed_request = session.prepare_request( req )

response = session.send( packed_request )

# expected output
# <class 'requests.models.Response'>
print( type(response), end='\n\n' )


# expected output:
'''
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "age": "5",
    "name": "Cute Cat"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "19",
    "Content-Type": "application/x-www-form-urlencoded",
    "Country": "USA",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.21.0",
    "X-Amzn-Trace-Id": "Root=1-602f79c1-14ba63af2327e16b7ad26863"
  },
  "json": null,
  "origin": "111.251.87.9",
  "url": "https://httpbin.org/post"
}
'''
print( response.text )