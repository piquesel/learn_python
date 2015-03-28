import datetime

def minutes(datetime1, datetime2):
    delta = datetime1 - datetime2
    print(delta)
    print(delta.seconds)
    delta_minutes = round(delta.seconds/60)
    return delta_minutes
    
print(minutes(datetime.datetime(2015, 3, 21, 15, 10, 20), datetime.datetime(2015, 3, 21, 15, 0, 10)))
    