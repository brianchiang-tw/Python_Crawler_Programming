from lxml import etree

parser = etree.HTMLParser()

text = '''
<div>
    <a href="https://www.google.com"> 古哥 </a>
    <a href="https://www.hinet.net"> 中華電信 </a>
    <a href="https://www.jd.com"> 京東商城 </a>
    <a href="https://www.microsoft.com"> 微軟 </a>
    <a href="https://www.ibm.com"> IBM </a>
</div>
'''

# index counting start form 1 in XPATH

#html = etree.parse( text, parser)
html = etree.HTML( text )

a1 = html.xpath('//a[1]')

#  古哥 
print( a1[0].text )

# https://www.google.com
print( a1[0].get('href') )

# ----------------------------
print('\n---')


a2 = html.xpath('//a[2]')

#  中華電信
print( a2[0].text )

# https://www.hinet.net
print( a2[0].get('href') )

# ----------------------------
print('\n---')

a_last = html.xpath('//a[last()]')

#  IBM
print( a_last[0].text )

# https://www.ibm.com
print( a_last[0].get('href') )

# ----------------------------
print('\n---')

'''
 微軟
https://www.microsoft.com

 IBM
https://www.ibm.com
'''
idx_larger_than_3 = html.xpath('//a[position()>3]')

for node in idx_larger_than_3:
    print( node.text )
    print( node.get('href') )
    print()

# ----------------------------
print('\n---')

second_node = html.xpath('//a[position()=2]')

#  中華電信
print( second_node[0].text )

# https://www.hinet.net
print( second_node[0].get('href') )