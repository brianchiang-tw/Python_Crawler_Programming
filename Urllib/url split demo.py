from urllib.parse import urlsplit, urlunsplit

result = urlsplit('https://search.jd.com/Searchprint;hello?keyword=Python從菜鳥到高手&enc=utf-8#comment')

print('scheme', result.scheme)