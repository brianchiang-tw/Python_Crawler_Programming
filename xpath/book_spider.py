from lxml import *
from lxml import etree
import requests
import json

def get_one_page(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        
        else:
            print('error')
            exit()
            return None
    

    except Exception:
        return None

# -----------------------------------------

def parse_one_page( html ):

    
    html = etree.HTML( html )

    items = html.xpath('//tr[@class="item"]')

    for item in items:

        book_information = item.xpath('td/p/text()')[0]
        book_info_tokens = book_information.split('/')

        #print( book_info_tokens )

        yield{
            'name': item.xpath('td/div/a/@title')[0],
            'url': item.xpath('td/div/a/@href')[0],
            'author': book_info_tokens[0],
            'publisher': book_info_tokens[-3],
            'date': book_info_tokens[-2],
            'price': book_info_tokens[-1],
        }

# -----------------------------------------

def save( content ):

    with open('top_250_books.txt', 'at', encoding='utf-8') as f:

        f.write( json.dumps(content, ensure_ascii=False) + '\n' )

# -----------------------------------------

def get_top_250_books( url ):

    source_page = get_one_page( url )

    for item in parse_one_page( source_page ):
        #print( item )
        save( item )


# -----------------------------------------

urls = ['https://book.douban.com/top250?start={}'.format( str(i) ) for i in range(0, 250, 25)  ]

print(urls)

for url in urls:
    print( url )
    get_top_250_books( url )
