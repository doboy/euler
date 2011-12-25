from utils import change, primeGen

n = 10

while change( n, tuple( primeGen( n ) ) ) < 5000:
    n += 1
else:
    print n
