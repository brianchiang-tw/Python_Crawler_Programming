import re

# ------------------------------------------

def search_all(pattern, string, flags=''):

    if flags:
        # regex flag is specified
        pat = re.compile(pattern, flags)

    else:
        # no regex flag
        pat = re.compile(pattern)

    search = re.findall(pat, string)

    if search:

        print(search)

    else:

        print('No search result')

# ------------------------------------------

# expected output:
# ['bike']
search_all(pattern=r'bike', string='bike')

print('\n\n')

# expected output:
# ['bike']
search_all(pattern=r'bike', string='my bike')

print('\n\n')

# expected output:
# ['bike', 'bike']
search_all(pattern=r'bike', string='This is a bike. This is my bike')

print('\n\n')


pattern = r'\d\d-a-[a-z]{3}'
string = '12-a-abc-54-a-xyz---78-A-ytr'

# expected output:
# ['12-a-abc', '54-a-xyz']
search_all(pattern, string)

pattern = r'(\d\d)-a-([a-z]{3})'
string = '12-a-abc-54-a-xyz---78-A-ytr'

# expected output:
# [('12', 'abc'), ('54', 'xyz')]
search_all(pattern, string)


print('\n\n')

pattern = r'(\d\d)-a-([a-z]{3})'
string = '12-a-abc-54-a-xyz---78-A-ytr'

# re.I : ignore letter case
# expected output:
# [('12', 'abc'), ('54', 'xyz'), ('78', 'ytr')]
search_all(pattern, string, re.I)

print('\n\n')

pattern = r'(\d\d)-a-([a-z]{3})'
string = '12-a-abc-54-a-xyz---78-A-ytr'

it = re.finditer(pattern, string, re.I)

for result in it:
    print( result.group(), end=' < ' )

    groups = result.groups()

    for group in groups:

        print(group, end = ' ')

    print('> ')