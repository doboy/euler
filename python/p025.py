from math import log10
from utils import fibGen

f, i = fibGen(), 1
while log10( f.next() ) < 999:
    i += 1
print i

# tags: fib
