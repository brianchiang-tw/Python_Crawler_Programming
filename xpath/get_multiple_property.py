from lxml import etree

parser = etree.HTMLParser()

html = etree.parse('demo.html', parser)

target_nodes = html.xpath('')