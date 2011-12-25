from utils import primeGen

for t in primeGen():
    if t > 8:
        break
    d = t

n = d * 3 // 7
while float( n + 1 ) / d < float( 3 ) / 7:
    n += 1

print n, d
