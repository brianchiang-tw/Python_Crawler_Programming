from urllib.parse import parse_qs, parse_qsl

query = 'name=可愛小貓咪&age=5'

# expected output
# {'name': ['可愛小貓咪'], 'age': ['5']}
print( parse_qs(query) )

print()

# expected output
# [('name', '可愛小貓咪'), ('age', '5')]
print( parse_qsl(query) )

print()

# --------------------------------------------

query = 'name=可愛小貓咪&age=5&name=可愛小狗狗&age=6'

# expected output
# {'name': ['可愛小貓咪', '可愛小狗狗'], 'age': ['5', '6']}
print( parse_qs(query) )
print()

# expected output
# [('name', '可愛小貓咪'), ('age', '5'), ('name', '可愛小狗狗'), ('age', '6')]
print( parse_qsl(query) )
print()