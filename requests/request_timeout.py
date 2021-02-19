import requests, requests.exceptions

try:
    response = requests.get('https://www.jd.com', timeout=0.01 )
    '''
    expected output:

    <!DOCTYPE html>
<html>
<head>
  <meta charset="gbk" />
  <title>京东台湾版-专业的综合网上购物商城</title>
  <meta name="keywords" content="网上购物,家电,手机,计算机,服装,国际,海外,居家,母婴,美妆,个护,食品
,京东,集运,全球" />
  <meta name="description

    '''
    print( response.text[:200] )

except requests.exceptions.Timeout as error:
    print( error )



# connection limit: 0.001 second
# read limit: 0.01 second

# expected output:
'''
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='www.jd.com', port=443): Max retries 
exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.VerifiedHTTPSConnection object at 0x0000015973EF7278>, 'Connection to www.jd.com timed out. (connect timeout=0.001)')) 
'''
#requests.get('https://www.jd.com', timeout=(0.001, 0.01) )

response = requests.get('https://www.jd.com', timeout=None )

print( response.status_code )