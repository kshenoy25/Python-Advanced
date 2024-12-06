# collections: counter, namedtuple, orderdict, defaultdict, deque
#rom collections import Counter
#from collections import namedtuple
#from collections import OrderedDict
#from collections import defaultdict
from collections import deque

#a = "aaaaaabbbbbcc"
#my_counter = Counter(a)
#print(my_counter.values())
#print(my_counter.items())
#print(my_counter.most_common(1))
#print(my_counter.most_common(1)[0][0])
#print(list(my_counter.elements()))

#Point = namedtuple("Point", "x y")
#pt = Point(1, 2)
#print(pt)

"""
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

"""

"""
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d['a'])

"""
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

#d.pop()
d.extend([4, 5])
d.extendleft([6, 7])
d.rotate(1)
print(d)