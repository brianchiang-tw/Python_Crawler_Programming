from lxml import etree

parser = etree.HTMLParser()

html = etree.parse('demo.html', parser)

result = html.xpath('//a[@href="https://www.jd.com"]/../@class')

# <class 'lxml.etree._ElementUnicodeResult'>
print(type(result[0]))

# class property of given parnet node: item2
print('class property of given parnet node:', result[0])

print('\n')

result = html.xpath('//a[@href="https://www.jd.com"]/parent::*/@class')

# <class 'lxml.etree._ElementUnicodeResult'>
print(type(result[0]))

# class property of given parnet node: item2
print('class property of given parnet node:', result[0] )

print('\n')

parent_node = html.xpath('//a[@href="https://www.jd.com"]/..')

# <class 'lxml.etree._Element'>
print(type(parent_node[0]))

# class property of given parent node: item2
print('class property of given parent node:', parent_node[0].get('class'))