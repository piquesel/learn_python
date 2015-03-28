import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
    (?P<last_name>[\w ]+),\s(?P<first_name>[\w ]+): \s # Last and first names
    (?P<score>[\d]+) # Score
''', string, re.X|re.M)

print(players)