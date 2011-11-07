from Prime import primeGen

gen = primeGen()
i, primeI = 1, gen.next()

while 2 * primeI * i < 10000000000:
    i+=2; gen.next()
    primeI = gen.next()

print primeI, i, 2*primeI*i
