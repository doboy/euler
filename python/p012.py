from utils import divisors, triangleGen

for n in triangleGen():
    if len( divisors( n ) ) > 500:
        break

print n
