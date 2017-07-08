#5906

import itertools
from fractions import gcd

max_multiplier = 5909
min_multiplier = 5000

def potential_denominator(n):
    '''
    Checks whether n is a potential denominator by finding any coprimes
    smaller than n raised to the fourth power can sum to give n
    '''
    l = []
    for j in range(n):
        # Append fourth powers of coprimes
        if gcd(j,n) == 1:
            l.append(((j**2)%n)**2%n)
    # Create all combinations of fourth powers
    it = itertools.combinations_with_replacement(l,2)
    # Generate any pairs that sum to n
    p = [x for x in it if sum(x)==n]
    return bool(p)

def potential_soltions(fourth, den_four):
    '''
    Checks whether there are any potential solutions with a denominator by
    pairing up fourth powers
    '''
    # Generate fourth powers that are coprime to the denominator
    possible_numerators = [x for x in fourth if gcd(x,den_four) == 1]
    it = itertools.combinations_with_replacement(possible_numerators, 2) #create all combinations of these fourth powers
    return [x for x in it if sum(x)>min_multiplier*den_four and sum(x)<max_multiplier*den_four and sum(x)%den_four == 0] # return a list in the correct range and it a potential solution (sum of fourth powers of numerator must be divisible by the fourth power of the denominator)

fourth = [x**4 for x in range(18)] # list of fourth powers

it = itertools.combinations_with_replacement(fourth,2)

sums_of_fourth_powers = [sum(x) for x in it if sum(x)>=min_multiplier and sum(x) <=max_multiplier] # generate sums of fourth powers of integers in possible range

for i in range(2,50):
    if potential_denominator(i):
        while len(fourth) ** 4< max_multiplier * i**4:
            fourth.append(len(fourth)**4) #add to fouth powers until we have enough
        ps = potential_soltions(fourth,i**4)
        if ps:
            for p in ps:
                if sum(p)/i**4 not in sums_of_fourth_powers:
                    print(i,p,sum(p)/i**4)
print(potential_denominator(34))
