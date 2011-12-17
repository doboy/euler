t, a, b  = 0, 0, 1
while b < 4 * 10 ** 6 :
    if not b % 2:
        t += b
    a, b = b, a + b
print t
