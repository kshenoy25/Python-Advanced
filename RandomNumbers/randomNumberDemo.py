import random


"""
mylist = list("ABSCDEFG")
#a = random.choices(mylist, k=3)

random.shuffle(mylist)
print(mylist)

"""

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))
