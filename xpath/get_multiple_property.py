from lxml import etree

parser = etree.HTMLParser()

html = etree.parse('demo.html', parser)

target_nodes = html.xpath('//a[@href="https://www.jd.com" or @href="https://www.hinet.net"]')


'''
Node text:  京東商城
Node URL: https://www.jd.com
Node text:  中華電信
Node URL: https://www.hinet.net
'''
for node in target_nodes:
    print(f'Node text: {node.text}')
    print(f'Node URL: {node.get("href")}')


print('\n')

# ---------------------------------------------

target_nodes = html.xpath('//a[contains(@href, "www") and ../@value="168"]')

'''
Node text:  中華電信
Node URL: https://www.hinet.net
'''
for node in target_nodes:
    print(f'Node text: {node.text}')
    print(f'Node URL: {node.get("href")}')