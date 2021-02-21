import re

# --------------------------------------

def match_pattern(pattern, string_list):

    pat = re.compile(pattern)
    

    for string in string_list:
        
        match = re.match(pat, string)

        if match is not None:
            print( match )
        
        else:
            print( 'No match result' )

# --------------------------------------

def search_pattern(pattern, string_list):

    pat = re.compile(pattern)
    

    for string in string_list:
        
        match = re.search(pat, string)

        if match is not None:
            print( match )
        
        else:
            print( 'No search result' )

# --------------------------------------

pattern = 'a+b+c+'
string_list = ['abc', 'aabc', 'bbabc', 'aaabbbcccxyz']

# expectd output:
'''
<re.Match object; span=(0, 3), match='abc'>
<re.Match object; span=(0, 4), match='aabc'>
No match result
<re.Match object; span=(0, 9), match='aaabbbccc'>
'''
match_pattern(pattern, string_list)

# --------------------------------------
print('\n\n\n')

pattern = '\d{3}-[a-z]{3}'
string_list = ['123-abc', '432-xyz', '1234-xyz', '1-xyzabc', '543-xyz^%ab']

# expected output:
'''
<re.Match object; span=(0, 7), match='123-abc'>
<re.Match object; span=(0, 7), match='432-xyz'>
No match result
No match result
<re.Match object; span=(0, 7), match='543-xyz'>
'''
match_pattern(pattern, string_list)

# --------------------------------------
print('\n\n\n')

pattern = '[a-z]?\d+'
string_list = ['1234', 'a123', 'ab432', 'b234abc']

# expected output:
'''
<re.Match object; span=(0, 4), match='1234'>
<re.Match object; span=(0, 4), match='a123'>
No match result
<re.Match object; span=(0, 4), match='b234'>
'''
match_pattern(pattern, string_list)

# --------------------------------------
print('\n\n\n')

pattern = '\w+@(\w+\.)*\w+\.com'

email_list = ['abc@126.com', 'test@mail.geekori.com', 'test-abc@hello.com', 'cat@animal.com.uk']
email_test = ['貓咪的email是cat@animal.com.uk']

# expected output:
'''
<re.Match object; span=(0, 11), match='abc@126.com'>
<re.Match object; span=(0, 21), match='test@mail.geekori.com'>
No match result
<re.Match object; span=(0, 14), match='cat@animal.com'>
'''
match_pattern(pattern, email_list)

# --------------------------------------
print('\n\n\n')

# expected output:
'''
<re.Match object; span=(0, 23), match='貓咪的email是cat@animal.com'>
'''
match_pattern(pattern, email_test)

# --------------------------------------
print('\n\n\n')

pattern = '[a-zA-Z0-9]+@(\w+\.)*\w+\.com'
# expected output:
'''
<re.Match object; span=(9, 23), match='cat@animal.com'>
'''
search_pattern(pattern, email_test)