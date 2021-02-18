from urllib3 import *
disable_warnings()
http = PoolManager()

url = 'http://localhost:5000'

while True:

    filename = input('input filename to upload: ')

    if not filename:
        break

    with open(filename, 'rb') as f:
        file_data = f.read()

    print('filename', filename)
    print('dbg', file_data)
    print()

    response = http.request('POST', url, fields={'file': (filename, file_data)})
    
    print( f'status code: {response.status}' )

    print( response.data.decode('utf-8') )
    
