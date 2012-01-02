from utils import fib, isPan

a, b = 0, 1
i = 2
while True:
    a, b = b, ( a + b ) % 10 ** 9
    if isPan( b ) and isPan( str( fib( i ) )[:9] ):
        break
    i += 1

print i
