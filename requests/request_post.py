import requests

payload = {
    'name' : 'Tom',
    'country' : 'USA',
    'age' : 18
}

r = requests.post('http://httpbin.org/post', data = payload )

# response text (string)
print( r.text )

print( '\n\n\n' )

# response json
response_json = r.json()
print( response_json )

for _key in response_json.keys():
    print( f'key: {_key} -> value: {response_json[_key]} ')
