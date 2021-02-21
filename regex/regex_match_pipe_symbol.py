import re

# --------------------------------------

def match_pattern(patter, string):

    match = re.match(pattern, string)

    if match:
        print( match.group() )

    else:
        print('No match')

# --------------------------------------

pattern = 'bike|car|truck'

# expected output:
# bike
match_pattern(pattern, string='bike')

# expected output:
# car
match_pattern(pattern, string='car')

# expected output:
# truck
match_pattern(pattern, string='truck')