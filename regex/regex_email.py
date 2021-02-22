import re

pattern = '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}'
email = 'cat@animal.com'

result = re.findall(pattern, email)

# cat@animal.com
print( result )

# ----------------------------------------------------
print('\n')

email = 'dog@animal'
result = re.findall(pattern, email)

# (Empty, no match)
print( result )

# ----------------------------------------------------
print('\n')

email = 'this is cat@animal.com, that is dog@zoo.com'
result = re.findall(pattern, email)

# ['cat@animal.com', 'dog@zoo.com']
print( result )