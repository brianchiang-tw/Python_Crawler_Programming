from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautful soup demo </title>
    
</head>

<body>
<div>
    <ul>
        <li class="item1"><a href="https://www.google.com"> google </a></li>
    </ul>
</div>
</body>

</html>
'''


soup = BeautifulSoup(html, 'lxml')


print( f'content of head node: {soup.head}')


