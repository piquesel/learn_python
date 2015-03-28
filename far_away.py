import datetime

def far_away(x):
    td = datetime.timedelta(x)
    nt = datetime.datetime.now() + td

print(far_away(seconds = 123))