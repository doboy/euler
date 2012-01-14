from datetime import datetime, timedelta

def dateGen( start, end, delta ):
    n = start
    while n <= end:
        yield n
        n += delta

print len( filter( lambda x : x.day == 6, dateGen( datetime( year=1901, month=1, day=6),
                                               datetime( year=2000, month=12, day=31),
                                               timedelta( days=7 ) ) ) )
