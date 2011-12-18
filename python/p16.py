def digitsGen( n ):
    while n:
        yield n % 10
        n //= 10

print sum( digitsGen( 2**1000 ) )
