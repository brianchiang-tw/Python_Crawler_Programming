import re

# ----------------------------------------

def search_pattern(pattern, string=''):

    pat = re.compile(pattern)

    match = re.search(pat, string)

    if match:
        
        print(f'full matching:', match.group() )

        for idx in range( len( match.groups() ) ):
            print(f'match subgroup idx: {idx+1}, subgroup= {match.group(idx+1)}')
    
    else:
        print( 'No match result')

# ----------------------------------------

pattern = r'^The'
string = 'The end.'

# expected output:
# full matching: The
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'^The'
string = 'end. The'

# expected output:
# No match result
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'The$'
string = 'end. The'

# expected output:
# full matching: The
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'The$'
string = 'The end.'

# expected output:
# No match result
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'\bthis'
string = "What's this?"

# expected output:
# full matching: this
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'\bthis'
string = "What'sthis?"

# expected output:
# No match result
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'\bthis\b'
string = "What's this?"

# expected output:
# full matching: this
search_pattern(pattern, string)

print('\n\n\n')

pattern = r'\bthis\b'
string = "What's thisa"

# expecte output:
# No match result
search_pattern(pattern, string)