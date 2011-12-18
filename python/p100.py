hash = set()
a = 2
while True:
    z = a * ( a - 1 )
    if z/2. in hash:
        print a
    hash.add( z )
    a += 1
        
