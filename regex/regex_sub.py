import re

result = re.sub('Bill', 'Mike', 'Bill is my son.')

# Mike is my son.
print( result )

# ('Mike is my son', 1)
result = re.subn('Bill', 'Mike', 'Bill is my son')

# ('Mike is my son', 1)
print( result )

# replacement result Mike is my son
print( 'replacement result', result[0] )

# times of replacement 1
print( 'times of replacement', result[1] )

print('\n\n')

pattern = r'([0-9])([a-z]+)'
replacement = r'Product number (\1 - \2)'
string = '01-1abc,02-2xyz,03-3def'

result = re.sub(pattern, replacement, string)
print( result )

print('\n\n')

pattern = r'([0-9])([a-z]+)'
replacement = r'Product number (\1 - \2)'
string = '01-1abc,02-2xyz,03-3def'

result = re.subn(pattern, replacement, string)
print( 'replacement result', result[0] )
print( 'times of replacement', result[1] )
