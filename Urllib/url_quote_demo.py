from urllib.parse import quote, unquote

keyword = "喵"

url = 'https://www.google.com/search?q=' + quote("貓咪")

print( url )

original = unquote( url )

print( original )