#Solution: 381654729

import itertools

s = "123456789"
a = itertools.permutations(s)
for t in a:
    s = ""
    for d in t:
        s += d
        if int(s) % len(s):
            break
    else:
        print(s)
