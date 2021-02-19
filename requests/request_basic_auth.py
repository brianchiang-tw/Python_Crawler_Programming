import requests

from requests.auth import HTTPBasicAuth

response = requests.get('http://localhost:5000', auth=HTTPBasicAuth('bill','1234'))

# expected output:
# 200
print( response.status_code )

# expected output
# success
print( response.text )