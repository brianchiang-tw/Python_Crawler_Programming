from bs4 import BeautifulSoup

html = '''
<html>
    <head><title>This is a demo page </title>
    </head>

    <body>
        <a href="a.html"> First Page </a>
        <a href="b.html"> Second Page </a>
    </body>
</html>
'''


soup = BeautifulSoup(html, 'lxml')


print('\nweb page title')
print('<' + soup.title.string + '>')

print('\nfirst anchor tag')
print('[' + soup.a["href"] + ']')

print('\n\n output html of all web page')
print( soup.prettify() )


'''

expected output:

web page title
<This is a demo page >

first anchor tag      
[a.html]


 output html of all web page
<html>
 <head>
  <title>
   This is a demo page
  </title>
 </head>
 <body>
  <a href="a.html">
   First Page
  </a>
  <a href="b.html">
   Second Page
  </a>
 </body>
</html>

'''