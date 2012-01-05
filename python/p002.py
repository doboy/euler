def fibGen( n ):
    a, b = 0, 1
    yield 0
    while b < n:
        yield b
        a, b = b, a + b

print sum( x for x in fibGen( 4 * 10 ** 6 ) if not x % 2 )
