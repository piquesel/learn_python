import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

#string = 'Perotto, Pier Giorgio'
contacts = re.search('''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4}),\s # Phone
    (?P<twitter>@[\w\d]+)?$ # Twitter
''', string,re.X)


print(contacts)
print(contacts.groupdict())

twitters = re.search(r'(@[\w\d]+)$', string, re.M)
print(twitters)