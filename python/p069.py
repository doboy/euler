from utils import primeGen, product

n, g = 1, primeGen()
t = next( g )

while n * t < 10 ** 6:
    n *= t
    t = next( g )

print n
