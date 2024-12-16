# unpacking refers to splitting up an iterable object and grabbing its individual elements

# basic unpacking
a, b, c = [1,2,3]
print(f"a: {a}, b: {b}, c: {c}\n")

# extended iterable unpacking with * which allows to collect multiple elements as a list/split up a list
a, b, *c =[1,2,3,4,5]
print(f"a: {a}, b: {b}, c: {c}\n")

# ignoring values when there is a need to put a variable somewhere but do not actually want to access
# it later on
# _ = anonymous variable and can use it multiple times
a, _, c = [1,2,3]

# unpacking nested structures
data = ("Alice", (25, "Engineer"))
name, (age, profession) = data


# unpacking in function arguments
def print_names(*names):
    for name in names:
        print(name)

print_names("Haley", "Kunal", "Parker")

# combining lists with unpacking

list1 = [1,2,3]
list2 = [4,5,6]
combined = [*list1, *list2]
print(f"Combined List: {combined}\n")

# unpacking dictionaries with **

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined_dict = {**dict1, **dict2}
print(f"Combined Dictionary: {combined_dict}\n")

# swapping variables using unpacking

x = 10
y = 20
print(f"Before Swap - x: {x}, y: {y}")
x, y = y, x
print(f"After Swap - x: {x}, y: {y}\n")