import re


def match_word(pattern, string):
    cur_match = re.match(pattern, string)

    if cur_match:

        # matching group
        print( cur_match.group() )

    # class name
    print( cur_match.__class__.__name__ )

    # type
    print( type(cur_match) ) 


# --------------------------------------

# expected output
'''
hello
Match
<class 're.Match'>
'''
match_word( pattern='hello', string='hello' )
print('\n\n')


# expected output
'''
NoneType
<class 'NoneType'>
'''
match_word( pattern='hello', string='world' )
print('\n\n')


# expected output
'''
hello
Match
<class 're.Match'>
'''
match_word( pattern='hello', string='hello world' )
print('\n\n')
