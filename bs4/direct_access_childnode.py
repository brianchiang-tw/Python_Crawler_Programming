from bs4 import BeautifulSoup

html='''
<html>
<head>
    <meta charset="UTF-8">
    <title>Direct access child node demo</title>
    <h>some demo text</h>
</head>
<body>
</body>
</html>
'''


soup = BeautifulSoup(html, 'lxml')


print( soup.head.contents )
'''
expected output
['\n', <meta charset="utf-8"/>, '\n', <title>Direct access child node demo</title>, '\n', <h>some demo text</h>, '\n']
'''


print()

print( soup.head.children )
'''
expected output (address may be different)
<list_iterator object at 0x000001E5A7806CF8>
'''