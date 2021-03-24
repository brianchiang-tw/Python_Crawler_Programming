from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful soup demo </title>
</head>

<body>
<div>
    <ul>
        <li class="item1" value1="1234" value2="hello world"><a href="https://www.google.com"> google.com</a></li>
        <li class="item2"><a href="https://www.jd.com"> 京東商城 </a></li>
        <li class="item3"><a href="https://www.taobao.com"> 淘寶網 </a></li>
        <li class="item4"><a href="https://www.bing.com"> bing search engine </a></li>
        <li class="item5"><a href="https://www.baidu.com"> Baidu </a></li>
    </ul>
</div>
</body>

</html>
'''

soup = BeautifulSoup(html, 'lxml')

print( f'\nhtml web page title name : {soup.title.name}' )
print( f'\nattribuee name and attribute value of 1st <li></li> node : \n{soup.li.attrs}')
print( f'\nattribute value of value1 in 1st <li></li> node : {soup.li.attrs["value1"]}')
print( f'\nattribute value of "value2" in 1st <li></li> node : {soup.li.attrs["value2"]}' )
print( f'\nattribute value of 1st <a></a> node : {soup.a["href"]}')
print( f'\nplaintext of 1st <a></a> node : {soup.a.string}')

'''

Expected output

html web page title name : title

attribuee name and attribute value of 1st <li></li> node :
{'class': ['item1'], 'value1': '1234', 'value2': 'hello world'}

attribute value of value1 in 1st <li></li> node : 1234

attribute value of "value2" in 1st <li></li> node : hello world

attribute value of 1st <a></a> node : https://www.google.com

plaintext of 1st <a></a> node :  google.com

'''