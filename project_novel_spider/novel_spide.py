from requests.api import head
import xlwt
import requests
from lxml import etree
import time

def get_one_page( url ):

    response = requests.get( url )

    status_code = response.status_code

    print( status_code )

    html = etree.HTML(response.text)
    
    book_information = html.xpath('//ul[@class="all-img-list cf"]/li')

    print( len(book_information) ) 
    #print( book_information )

    for book in book_information:

        #print( book.xpath('div[2]/h4/a/text()')[0] )

        # category
        style_1 = book.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = book.xpath('div[2]/p[1]/a[3]/text()')[0]

        yield{
            'Title': book.xpath('div[2]/h4/a/text()')[0],
            'Author': book.xpath('div[2]/p[1]/a[1]/text()')[0],
            'Category': style_1 + ' ' +style_2,
            'Progress': book.xpath('div[2]/p[1]/span/text()')[0],
            'Introduction': book.xpath('div[2]/p[2]/text()')[0].strip(),
        }




# ------------------------------------------------------------

#get_one_page('http://www.qidian.com/all/?page=1')

# CSV file header
header = ['Title','Author','Category','Progress','Introduction']

book = xlwt.Workbook(encoding='utf-8')

sheet = book.add_sheet('novels')

header_length = len(header)
for i in range( header_length ):
    
    sheet.write(0, i, header[i])

novel_urls = ['https://www.qidian.com/all/?page={}'.format( str(i) ) for i in range(1, 11)]

novel_index = 1

for url in novel_urls:

    novels = get_one_page( url )

    for novel in novels:
        
        print(f'current novel: {novel}' )

        time.sleep( 0.1 )

        sheet.write(novel_index, 0, novel['Title'])
        sheet.write(novel_index, 1, novel['Author'])
        sheet.write(novel_index, 2, novel['Category'])
        sheet.write(novel_index, 3, novel['Progress'])
        sheet.write(novel_index, 4, novel['Introduction'])

        novel_index += 1


book.save('novels.xls')


