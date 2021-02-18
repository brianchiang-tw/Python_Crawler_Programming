from urllib3 import *
import re

disable_warnings()

http = PoolManager()

url = 'https://list.tmall.com/search_product.htm?q=cat&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'

# ----------------------------------------------------

def str_to_headers( file ):

    header_Dict = {}

    with open(file, 'r') as f:

        headers_text = f.read()

        headers = re.split('\n', headers_text)

        for header in headers:

            result = re.split(':', header, maxsplit=1)

            # update key-value pair
            header_Dict[ result[0] ] = result[1]
    
    return header_Dict

# ----------------------------------------------------

headers = str_to_headers('headers.txt')

print( headers )

response = http.request('GET', url, headers=headers )

data = response.data.decode('GB18030')
#data = response.data.decode('utf-8')

print( data )