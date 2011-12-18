m, i, n = 1, 2, 600851475143

while n > 1:
    while not n % i:
        n /= i
        m = i
    i += 1

print m
