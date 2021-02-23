from lxml import etree

# Create HTML parser
parser = etree.HTMLParser()

# parse given html file with HTML parser
html = etree.parse('demo.html', parser)

target_nodes = html.xpath('//a[@href="https://www.hinet.net"]')

# There are total 1 nodes with url = http://www.hinet.net
print(f'There are total {len(target_nodes)} nodes with url = http://www.hinet.net')

# 中華電信
for node in target_nodes:
    print(f'Text of node: {node.text}')


# -----------------------------------------------------
print()


target_nodes = html.xpath('//a[contains(@href,"www")]')

# There are total 5 nodes with url and url contains "www"
print(f'There are total {len(target_nodes)} nodes with url and url contains "www"')

'''
Text of node:  古哥
URL of node: https://www.google.com
Text of node:  京東商城
URL of node: https://www.jd.com
Text of node:  微軟
URL of node: https://www.microsoft.com
Text of node:  IBM
URL of node: https://www.ibm.com
Text of node:  中華電信
URL of node: https://www.hinet.net
'''
for node in target_nodes:
    print(f'Text of node: {node.text}')
    print(f'URL of node: {node.get("href")}')


# -----------------------------------------------------
print()

target_nodes = html.xpath('//a[contains(@href,"www")]/@href')

'''
URL of node: https://www.google.com
URL of node: https://www.jd.com
URL of node: https://www.microsoft.com
URL of node: https://www.ibm.com
URL of node: https://www.hinet.net
'''
for node in target_nodes:
    print(f'URL of node: {node}')