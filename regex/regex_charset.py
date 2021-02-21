import re
# ------------------------------------    

def match_pattern(pattern, string=''):

    match = re.match(pattern, string)

    if match:
        print( match.group() )
    
    else:
        print( 'No match result')

# ------------------------------------   

pattern='[ab][cd][ef][gh]'

# expected output:
# adfh
match_pattern(pattern, 'adfh')

pattern = '[ab][cd][ef][gh]'

# ---------------------------------

# expected output:
# bceg
match_pattern(pattern, 'bceg')

# ---------------------------------

pattern = '[ab][cd][ef][gh]'

# expected output:
# No match reult
match_pattern(pattern, 'abceh')

# ---------------------------------

pattern = 'ab[cd][ef][gh]'

# expected output:
# abceh
match_pattern(pattern, 'abceh')

# ---------------------------------

pattern = 'abcd|efgh'

# expected output:
# efgh
match_pattern(pattern, 'efgh')