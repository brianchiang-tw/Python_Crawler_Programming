from lxml import etree

parser = etree.HTMLParser()

# parse demo.html with html parser
html = etree.parse('demo.html', parser)

# select all <a> in children nodes
nodes = html.xpath('//a')

print('\n')

print(f'There are total {len(nodes)} <a> nodes')

print( nodes )


'''
url: https://www.google.com
text:  古哥
url: https://www.jd.com
text:  京東商城
url: https://www.microsoft.com
text:  微軟
url: https://www.ibm.com
text:  IBM
url: https://www.hinet.net
text: 中華電信
'''
for a_node in nodes:

    print(f'url: {a_node.get("href")}')
    print(f'text: {a_node.text}')