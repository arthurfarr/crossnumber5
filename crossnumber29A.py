#Possibles: [232, 520, 520, 584, 800, 808]

import itertools

l = []
for i in range(1,int(1000**0.5)):
    l.append(i**2)

sums = [sum(t) for t in itertools.combinations(l,2)]
sums.sort()

print([x for x in sums if x+1 in sums and x+2 in sums])
