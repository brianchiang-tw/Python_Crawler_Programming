import re

result = re.split(';', 'Bill;Mike;John')

# expected output:
# ['Bill', 'Mike', 'John']
print( result )

pattern = r'[,;.\s]+'
string = 'a,b,,d,d;x   c;d.  e'
result = re.split(pattern, string)

# expected output:
# ['a', 'b', 'd', 'd', 'x', 'c', 'd', 'e']
print( result )

print('\n\n')

pattern = r'[a-z]{3}-[0-9]{2}'
string = 'testabc-4312productxyz-43abill'

result = re.split(pattern, string)
# expected output:
# ['test', '12product', 'abill]
print( result )

print('\n\n')

pattern = r'[a-z]{3}-[0-9]{2}'
string = 'testabc-4312productxyz-43abill'

# max split times = 1
result = re.split(pattern, string, maxsplit=1)

# expected output:
# ['test', '12productxyz-43abill']
print(result)

