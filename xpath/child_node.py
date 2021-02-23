from lxml import etree

parser = etree.HTMLParser()

# parse given html file with html parser
html = etree.parse('demo.html', parser)

# slect <a> directly under <li>
nodes = html.xpath('//li/a')

# There are total 5 nodes
print(f'There are total {len(nodes)} nodes')

# [<Element a at 0x28c32ab3d48>, <Element a at 0x28c32ab3d88>, <Element a at 0x28c32ab3dc8>, <Element a at 0x28c32ab3e08>, <Element a at 0x28c32ab3e48>]
print( nodes )

'''
Text:  古哥
URL: https://www.google.com
Text:  京東商城
URL: https://www.jd.com
Text:  微軟
URL: https://www.microsoft.com
Text:  IBM
URL: https://www.ibm.com
Text: 中華電信
URL: https://www.hinet.net
'''
for node in nodes:
    print(f'Text: {node.text}')
    print(f'URL: {node.get("href")}')

# -----------------------------------------------

print('\n')

nodes = html.xpath('//ul//a')

# [<Element a at 0x28c32ab3d48>, <Element a at 0x28c32ab3d88>, <Element a at 0x28c32ab3dc8>, <Element a at 0x28c32ab3e08>, <Element a at 0x28c32ab3e48>]
print( nodes )

'''
Text:  古哥
URL: https://www.google.com
Text:  京東商城
URL: https://www.jd.com
Text:  微軟
URL: https://www.microsoft.com
Text:  IBM
URL: https://www.ibm.com
Text: 中華電信
URL: https://www.hinet.net
'''
for node in nodes:
    print(f'Text: {node.text}')
    print(f'URL: {node.get("href")}')

# -----------------------------------------------

print('\n')

nodes = html.xpath('//ul/a')

# []
print( nodes )

for node in nodes:
    print(f'Text: {node.text}')
    print(f'URL: {node.get("href")}')