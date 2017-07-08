#69

d = [str(i) for i in range(10)]

for i in range(60,70):
    l = [x for x in str(i**2)] + [x for x in str(i**3)]
    l.sort()
    if l == d:
        print(i)
