from lxml import etree

parser = etree.HTMLParser()

text = '''
<html>
<head>
    <meta charset="UTF-8">
    <title> xpath demo </title>
</head>
<body class="item">
<div>
    <ul class="item">
        
        <li class="item1">
            <a href="https://www.google.com"> 古歌 </a>
        </li>

        <li class="item2">
            <a href="https://www.microsoft.com"> 微軟 </a>
            <value url="https://www.hinet.net">
            <value url="https://www.yahoo.com">
        </li>
        
        <li class="item3">
            <a href="https://www.pchome.com.tw"> PCHOME </a>
            <a href="https://www.mit.edu"> 麻省理工　</a>
        </li>

        <li class="item4" value="168">
            <a href="https://www.nasdas.com"> NASDAQ </a>
        </li>

        <li class="item5">
            <a href="https://www.youtube.com"> Youtube </a>
        </li>

    </ul>
</div>
</body>
</html>
'''


html = etree.HTML(text)

target_node = html.xpath('//li[1]/ancestor::*')

# html->body->div->ul
print( '->'.join( node.tag for node in target_node ) )


# ---------------------------------
print('\n---')

target_node = html.xpath('//li[1]/ancestor::*[@class="item"]')

# body, ul
print( ', '.join( node.tag for node in target_node) )

# ---------------------------------
print('\n---')

target_node = html.xpath('//li[4]/attribute::*')

# item4, 168
print(', '.join( target_node))

# ---------------------------------
print('\n---')

target_node = html.xpath('//li[3]/child::*')

'''
URL:  https://www.pchome.com.tw
Text:   PCHOME
URL:  https://www.mit.edu
Text:   麻省理工
'''
for node in target_node:

    print('URL: ', node.get('href') )
    print('Text: ', node.text )

# ---------------------------------
print('\n---')

target_node = html.xpath('//li[2]/descendant::value')

'''
URL: https://www.hinet.net
URL: https://www.yahoo.com
'''
for node in target_node:

    print('URL:', node.get('url') )

# ---------------------------------
print('\n---')


target_node = html.xpath('//li[1]/following::*')

# li, a, value, value, li, a, a, li, a, li, a
print(', '.join( node.tag for node in target_node) )


# ---------------------------------
print('\n---')


target_node = html.xpath('//li[1]/following::*[ position() > 4]')

# li, a, a, li, a, li, a
print(', '.join( node.tag for node in target_node) )


# ---------------------------------
print('\n---')


target_node = html.xpath('//li[1]/following-sibling::*')

# li, li, li, li
print(', '.join( node.tag for node in target_node) )