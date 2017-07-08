#Possibles: [71193, 94981, 98671, 99301]

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

l=[]
for i in range(1,100000):
    if sum(factors(i)) == 100000:
        l.append(i)

print(l)
