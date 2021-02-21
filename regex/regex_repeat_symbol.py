import re

def match_pattern(pattern, string=''):

    match = re.match(pattern, string)

    if match:
        print( match )
    
    else:
        print( 'No match result')

# -------------------------------------

pattern = 'a*'
string_list = ['', 'a', 'aa', 'baa']

# expected output:
'''
<re.Match object; span=(0, 0), match=''>
<re.Match object; span=(0, 1), match='a'>
<re.Match object; span=(0, 2), match='aa'>
<re.Match object; span=(0, 0), match=''>
'''
for string in string_list:
    match_pattern(pattern, string)


# -----------------------------------------
print('\n\n\n')

pattern='a+'


# expected output:
'''
No match result
<re.Match object; span=(0, 1), match='a'>
<re.Match object; span=(0, 2), match='aa'>
No match result
'''
for string in string_list:
    match_pattern(pattern, string)

# -----------------------------------------
print('\n\n\n')

pattern = '(abc)+'

match_pattern(pattern, string='abcabcabc')

# -----------------------------------------
print('\n\n\n')

pattern = '\w?wow(\d?)+'

# expected output:
# <re.Match object; span=(0, 4), match='awow'>
match_pattern(pattern, string='awow')

# expected output
# <re.Match object; span=(0, 7), match='awow123'>
match_pattern(pattern, string='awow123')

# expected output:
# <re.Match object; span=(0, 5), match='wow12'>
match_pattern(pattern, string='wow12')

# expected output:
# No match result
match_pattern(pattern, string='ow12')