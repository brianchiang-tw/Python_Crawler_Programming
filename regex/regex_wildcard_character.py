import re



# ------------------------------------    

def match_pattern(pattern, string=''):

    match = re.match(pattern, string)

    if match:
        print( match.group() )
    
    else:
        print( 'No match result')

# ------------------------------------    

def search_pattern(pattern, string=''):

    search = re.search(pattern, string)

    if search:
        print( search.group() )
    
    else:
        print( 'No search result')

# ------------------------------------    

pattern = '.ind'

# expected output:
# bind
match_pattern(pattern, string='bind')

# expected output:
# No match result
match_pattern(pattern, string='ind')

# expected output:
# bind
match_pattern(pattern, string='binding')

# expected output:
# bin
match_pattern(pattern, string='bin')

# expected output:
# No match result
match_pattern(pattern, string='<bind>')

# --------------------------------------------

search_pattern(pattern, string='<bind>')

pattern_1 = '3.14'
pattern_2 = '3\.14'

# expected output:
# 3.14
match_pattern(pattern_1, string='3.14')

# expected output:
# 3314
match_pattern(pattern_1, string='3314')

# expected output:
# 3.14
match_pattern(pattern_2, string='3.14')

# expected output:
# No match result
match_pattern(pattern_2, string='3314')