from lxml import etree

parser = etree.HTMLParser()

# <class 'lxml.etree.HTMLParser'>
print( type(parser) )

tree = etree.parse('test.html', parser)

root = tree.getroot()

result = etree.tostring(root, encoding='utf-8', pretty_print=True, method='html')

# <class 'bytes'>
print( type(result) )

'''
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title> This is a demo website </title>
    </head>
    <body>
    </body>
</html>
'''
print( str(result, 'utf-8') )

# html
print( root.tag )

# language = en
print( 'language = ', root.get('lang') )

# charset = UTF-8
print( 'charset = ', root[0][0].get('charset') )

# title =   This is a demo website
print( 'title = ', root[0][1].text )