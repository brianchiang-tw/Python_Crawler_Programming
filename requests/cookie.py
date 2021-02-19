import requests

response_1 = requests.get('http://www.baidu.com')

cookies_1 = response_1.cookies

# expected output
# <class 'requests.cookies.RequestsCookieJar'>
print( type(cookies_1) )

# expected output
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print( cookies_1 )

# expected output
# key: BDORZ -> value: 27315
for _key, _value in cookies_1.items():
    print( f'key: {_key} -> value: {_value}' )


# ------------------------------
print('\n\n\n')

headers = {
    'Honst': 'www.jianshu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',     
    'Cookie': 'locale=zh-CN; __yadk_uid=JXO1fXVkRuSRZOhXbOSVjoKAo1VpesO8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221778b2affd1856-0084f11702c69d-73e3566-908050-1778b2affd2999%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221778b2affd1856-0084f11702c69d-73e3566-908050-1778b2affd2999%22%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2'
}



response_2 = requests.get('https://www.jianshu.com', headers=headers)

response_2_text = response_2.text

# expected output
# <class 'str'>
print( type(response_2_text) )
print( response_2_text[:200] )


# ------------------------------
print('\n\n\n')

headers = {
    'Honst': 'www.jianshu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',     
}

cookies = 'locale=zh-CN; __yadk_uid=JXO1fXVkRuSRZOhXbOSVjoKAo1VpesO8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221778b2affd1856-0084f11702c69d-73e3566-908050-1778b2affd2999%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221778b2affd1856-0084f11702c69d-73e3566-908050-1778b2affd2999%22%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; read_mode=day; default_font=font2'

cooker_jar = requests.cookies.RequestsCookieJar()

for cookie_key_value_pair in cookies.split(';'):

    cookie_key, cookie_value = cookie_key_value_pair.split('=', maxsplit=1)

    cooker_jar.set(cookie_key, cookie_value)


response_3 = requests.get('https://www.jianshu.com/', cookies=cooker_jar, headers=headers)

response_3_text = response_3.text

# expected output
# <class 'str'>
print( type(response_3_text) )
print( response_3_text[:200] )