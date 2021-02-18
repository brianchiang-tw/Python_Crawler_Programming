import requests

data = {
    'name':'貓咪',
    'country':'香港',
    'age':5
}

r = requests.get('http://httpbin.org/get?name=狗狗&country=澳門&age=6', params=data )

print( r.text )

print('\n\n\n')

request_json = r.json()
print( request_json )

print('\n\n\n')

for key in request_json['args']:

    print( f'key: {key} -> value: {request_json["args"][key]}' )