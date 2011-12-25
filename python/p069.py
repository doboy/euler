from utils import primeGen, product

n, g = 1, primeGen()
while True:
    t = next( g )
    if n * t > 1000000:
        break
    n *= t

print n
