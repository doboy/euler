from utils import factors

i = 1
while True:
    if len( factors( i ) ) == len( factors( i + 1 ) ) == len( factors( i + 2 ) ) == \
            len( factors( i + 3 ) ) == 4:
        break
    i += 1

print i
