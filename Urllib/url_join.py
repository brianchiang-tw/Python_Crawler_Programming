from urllib.parse import urljoin

# expected output
# https://www.jd.com/index.html
print( urljoin('https://www.jd.com', 'index.html') )

# expected output
# https://www.taobao.com
print( urljoin('https://www.jd.com', 'https://www.taobao.com') )

# expected output
# https://www.taobao.com/index.html
print( urljoin('https://www.jd.com', 'https://www.taobao.com/index.html') )

# expected output
# https://www.jd.com/index.php?name=Meow&age=5
print( urljoin('https://www.jd.com/index.php', '?name=Meow&age=5') )

# expected output
print( urljoin('https://www.jd.com/index.php?value=123', '?name=Meow'))