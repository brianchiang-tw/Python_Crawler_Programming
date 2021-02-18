import requests

response = requests.get('https://cdn.pixabay.com/photo/2017/11/20/14/01/kitten-2965641_1280.jpg')

with open('cute_cat.jpg', 'wb') as f:

    # save image binary to local jpg file
    f.write( response.content )