from utils import primeGen

gen = primeGen()
i, primeI = 1, next( gen )

while 2 * primeI * i < 10 ** 9:
    next( gen )
    primeI = next( gen )
    i += 2
print i

# RELOOK
