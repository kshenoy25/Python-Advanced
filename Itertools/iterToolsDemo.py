# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import groupby

def smaller_smaller_than_3(x):
    return x < 3
a = [1,2,3,4]
group_obj = groupby(a, key=smaller_smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
#print(list(group_obj))







"""
from itertools import accumulate
import operator
a = [1,2,5,3,4]
acc = accumulate(a, func = max)
#acc = accumulate(a, func = operator.mul)
print(a)
print(list(acc))

"""

"""
from itertools import combinations, combinations_with_replacement
a = [1,2,3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_w_replacement = combinations_with_replacement(a, 2)
print(list(comb_w_replacement))
"""

""""
from itertools import permutations
a = [1,2,3]
perm = permutations(a, 2)
print(list(perm))

"""

"""
from itertools import product, repeat

a = [1,2]
b = [3]
prod  = product(a,b, repeat=2)
print(list(prod))
"""
