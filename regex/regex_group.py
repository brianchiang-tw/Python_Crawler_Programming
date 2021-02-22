import re
from typing import Match

# ----------------------------------------------

def match_pattern(pattern, string=''):

    pat = re.compile(pattern)

    match = re.match(pat, string)

    if match:
        
        print(f'full matching', match.group() )

        for idx in range( len( match.groups() ) ):
            print(f'match subgroup idx: {idx+1}, subgroup= {match.group(idx+1)}')
    
    else:
        print( 'No match result')

# ----------------------------------------------
        
pattern = '(\d{3})-(\d{4})-([a-z]{2})'

# expected output:
'''
full matching 123-4567-xy
match subgroup idx: 1, subgroup= 123
match subgroup idx: 2, subgroup= 4567
match subgroup idx: 3, subgroup= xy
'''
match_pattern(pattern, string='123-4567-xy')


# ----------------------------------------------
print('\n\n\n')

pattern = '(\d{3}-\d{4})-([a-z]{2})'

# expected output:
# full matching 123-4567-xy
# match subgroup idx: 1, subgroup= 123-4567
# match subgroup idx: 2, subgroup= xy
match_pattern(pattern, string='123-4567-xy')


# ----------------------------------------------
print('\n\n\n')

pattern = '\d{3}-\d{4}-([a-z]{2})'
# expected output:
# full matching 123-4567-xy
# match subgroup idx: 1, subgroup= xy
match_pattern(pattern, string='123-4567-xy')

# ----------------------------------------------
print('\n\n\n')

pattern = '\d{3}-\d{4}-[a-z]{2}'

# expected output:
# full matching 123-4567-xy
match_pattern(pattern, string='123-4567-xy')
