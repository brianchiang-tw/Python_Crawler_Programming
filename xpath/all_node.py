from lxml import etree

# ------------------------------------------

def print_node_tree(node, indent):

    print( indent + node.tag )
    indent += '    '
    children = node.getchildren()

    # DFS print node tree
    if len(children) > 0:
        for i in range( len(children) ):
            print_node_tree( children[i], indent)

    return
# ------------------------------------------


parser = etree.HTMLParser()

# parse given html file with HTML parser
html = etree.parse('demo.html', parser)

# all child nodes
nodes = html.xpath('//*')

print( f'There are total {len(nodes)} nodes')


'''
There are total 17 nodes
html head meta title body div ul li a li a li a li a li a
'''

# output all nodes in HTML file
for i in range(0, len(nodes) ):
    print( nodes[i].tag, end= ' ')

print('\n')    



'''
html
    head
        meta
        title
    body
        div
            ul
                li
                    a
                li
                    a
                li
                    a
                li
                    a
                li
                    a
'''

root_node = nodes[0]
print_node_tree(node=root_node, indent='')

