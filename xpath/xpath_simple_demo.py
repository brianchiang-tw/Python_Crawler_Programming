from lxml import etree

parser = etree.HTMLParser()
tree = etree.parse('test.html', parser)

titles = tree.xpath('/html/head/title')

#  This is a demo website
if len(titles) > 0:
    print( titles[0].text )



html = '''
<div>
    <ul>
        <li class="item1"><a href="https://www.google.com"> 古哥　</a></li>
        <li class="item2"><a href="https://www.pchome.com.tw"> PCHOME購物城　</a></li>
        <li class="item3"><a href="https://www.jd.com"> 京東商城 </a></li>
    </ul>
</div>
'''

tree = etree.HTML( html )

target = tree.xpath("//li[@class='item2']")

# https://www.pchome.com.tw  PCHOME購物城
if len(target) > 0:
    print( target[0][0].get('href'), target[0][0].text )