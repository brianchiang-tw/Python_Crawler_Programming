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