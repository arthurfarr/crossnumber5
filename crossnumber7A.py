#145

import itertools
import math

def factsum(t):
    return sum([math.factorial(int(d)) for d in t])

iterable = itertools.combinations_with_replacement("1234567890",3)

for n in iterable:
    n = list(n)
    n.sort()
    fsum = list(str(factsum(n)))
    fsum.sort()
    if fsum == n:
        print(factsum(n))
