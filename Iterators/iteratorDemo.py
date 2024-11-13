# iterators are advanced Python concepts that allow for efficient looping and memory management. Iterators provide a way to access elements
# of a collection sequentially without exposing the underlying structure

"""

my_list = [1, 2, 3, 4, 5, 6]

for i in my_list:
    print(i)

it = iter(my_list)

print(it)


"""
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = TopTen()

for i in values:
    print(i)