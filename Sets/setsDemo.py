# sets: unordered, mutable, no duplicates

mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(3)


#for i in mySet:
#    print(i)

#num = 10
#if num in mySet:
#    print(f"{num} is in your set!")
#else:
#    print(f"{num} is not in your set!")

"""
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7,13}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

n = evens.intersection(primes)
print(n)

"""
setA  = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

#diff = setA.difference(setB)
#diff = setB.difference(setA)
#diff = setB.symmetric_difference(setA)
#print(diff)

#setA.update(setB)
setA.difference_update(setB)
print(setA)