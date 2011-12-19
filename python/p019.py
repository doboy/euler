from datetime import datetime, timedelta
from utils import dateGen

print len( filter( lambda x : x == 6, dateGen( datetime( year=1901, month=1, day=6),
                                               datetime( year=2000, month=12, day=31),
                                               timedelta( days=7 ) ) ) )
