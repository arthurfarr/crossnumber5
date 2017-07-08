#Possibles: [100001, 101101, 110011, 111111, 200002, 798644]

def is_pal(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

l = []
for i in range(100000,1000000):
    if is_pal(i**2):
        l.append(i)
print(l)
