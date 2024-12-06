#my_string = "Hello World"
#print(my_string.replace("Hello", "Bye Bye"))
#print(my_string.count("o"))
#print(my_string.find("o"))

"""
my_string = "how,are,you,doing"
my_list = my_string.split(",")
new_string = "".join(my_list)
print(new_string)
print(my_list)

"""
from timeit import default_timer as timer

my_list = ['a'] * 1000000
#print(my_list)

start = timer()
# bad python code
# an expensive method
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)



# good python code
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)