# lambda arguments: expression

"""

add10 = lambda x: x + 10
print(add10(10))

# without using lambda
def add10_func(x):
    return  x + 10

mult = lambda x, y: x * y
print(mult(122, 5))

"""
from functools import reduce

"""

points2D = [(1,2),(15,1),(5,-1),(10,4)]

#def sort_by_y(x):
#    return x[1]

# list was sorted according to the y index
points2D_sorted = sorted(points2D, key= lambda x: x[1])
print(points2D)
print(points2D_sorted)

"""

"""
points2D = [(1,2),(15,1),(5,-1),(10,4)]

#def sort_by_y(x):
#    return x[1]

# list was sorted according to the y index
points2D_sorted = sorted(points2D, key= lambda x: x[0]+ x[1])
print(points2D)
print(points2D_sorted)

"""

# map(func, seq)
a1 = [1,2,3,4,5]
b1 = map(lambda x: x*2, a1)
print(list(b1))

# using list comprehension syntax
c1 = [x*2 for x in a1]
print(c1)

# filter(func, seq) must return True or False
a2 = [1,2,3,4,5,6]
b2 = filter(lambda x: x%2 == 0, a2)
print(list(b2))

c2 = [x for x in a2 if x % 2 == 0]
print(list(c2))

# reduce(func, seq)
a3 = [1,2,3,4,5]
product_a = reduce(lambda x, y: x*y, a3)
print(product_a)

