from utils import primeGen, isPrime, isSquare, isEven

def Goldbach( c ):
    for p in primeGen( c ):
        if isEven( c - p ) and isSquare( ( c - p ) / 2 ):
            return True

c = 4
while isEven( c ) or isPrime( c ) or Goldbach( c ):
    c += 1

print c
