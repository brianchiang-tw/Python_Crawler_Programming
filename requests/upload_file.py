import requests

upload_file = open('cute_cat.jpg', 'rb')

print( type(upload_file) )

file_param = {'file': upload_file}
response = requests.post('http://httpbin.org/post', files=file_param )

print( response.text[:100] )