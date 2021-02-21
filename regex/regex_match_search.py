import re


# --------------------------------------------
def match_pattern( pattern, string ):

    match = re.match(pattern, string)
    if match:
        print('Match result: ', match.group() )
    
    else:
        print('No Match')

# --------------------------------------------    

def search_pattern( pattern, string):

    search = re.search(pattern, string)

    if search:
        print('Search result: ', search.group() )
    
    else:
        print('None')

# --------------------------------------------   

# expected output:
# No Match
match_pattern(pattern='python', string='we love python')

# expected output:
# Search result:  python
search_pattern(pattern='python', string='we love python')
