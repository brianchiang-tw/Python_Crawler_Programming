from urllib.parse import urlencode, urljoin

params = {
    'name': '貓咪',
    'country': '貓星球',
    'age': 5
}

base_url = 'https://www.google.com?'

# expected output
# https://www.google.com?name=%E8%B2%93%E5%92%AA&country=%E8%B2%93%E6%98%9F%E7%90%83&age=5
url = urljoin( base_url, '?' + urlencode(params) )

print( url )