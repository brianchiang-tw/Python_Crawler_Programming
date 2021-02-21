import re



# -------------------------------------

def match_pattern(pattern, string):

    match = re.match(pattern, string)
    
    if match:
        print( type( match.group() ) )
        print( match.group() )
    
    else:
        print('No match')

# -------------------------------------

pattern = 'Bill|Mike|John'

# expected output
#<class 'str'>
# Bill
match_pattern(pattern, string='Bill')

# expected output
#<class 'str'>
# Bill 
match_pattern(pattern, string='Bill: my friend')

# -------------------------------------

def match_search(pattern, string):

    match = re.search(pattern, string)
    
    if match:
        print( type( match.group() ) )
        print( match.group() )
    
    else:
        print('No matched search')

# -------------------------------------

# expected output:
# <class 'str'>
# Mike
match_search(pattern, string="Where is Mike?")

