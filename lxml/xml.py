from lxml import etree

tree = etree.parse('products.xml')

# <class 'lxml.etree._ElementTree'>
print( type(tree) )
print('\n')

xml_content = etree.tostring(tree, encoding='utf-8')
# <class 'bytes'>
print( type(xml_content) )

print('\n')

'''
<products>
    <product id="0001">
        <name>Cell phone</name>
        <price>4500</price>
    </product>
    <product id="0002">
        <name>Computer</name>
        <price>6000</price>
    </product>
</products>
'''
print( str(xml_content, 'utf-8') )

# get root node
root = tree.getroot()

# <class 'lxml.etree._Element'>
print( type(root) )

# root: products
print('root: ', root.tag)

children = root.getchildren()
print('Output product information')

'''
product id =  0001
name =  Cell phone
price =  4500

product id =  0002
name =  Computer
price =  6000

'''
for child in children:

    print('product id = ', child.get('id') )
    print('name = ', child[0].text )
    print('price = ', child[1].text )

    print()


# ----------------------------------
print('\n\n\n')

root_2 = etree.fromstring('''
<products>
    <product1 name="iPhone"/>
    <product2 name="iPad"/>
</products>
''')


print('root=', root_2.tag)

children = root_2.getchildren()

'''
root= products
product1 name =  iPhone
product2 name =  iPad
'''
for child in children:
    print( child.tag, 'name = ', child.get('name') )
