def primeGen():
    yield 2
    primesSoFar = [ 2 ]
    i = 3
    while True:
        for prime in primesSoFar:
            if not i % prime:
                break
        else:
            primesSoFar.append( i )
            yield i
        i += 1

    
