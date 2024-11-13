# decorators are a powerful and flexible feature in python that allows you to modify the behavior of a function or class method
# they are commonly used to add functionality to functions or methods without modifying their actual code

"""
# function copy
def welcome():
    return "Welcome to Decorators"

welcome()

wel = welcome()
print(wel)
del welcome
print(wel)
"""

"""
# closures

def main_welcome(msg):
    #msg = "Welcome "
    def sub_welcome_method():
        print("Welcome to the advanced python course")
        print(msg)
        print("Please learn these concepts properly")

    return  sub_welcome_method()
main_welcome("Welcome everyone")


def new_welcome(func, lst):
    #msg = "Welcome "
    def new_sub_welcome_method():
        print("Welcome to the advanced python course")
        print(func(lst))
        #func("Welcome everyone to this tutorial")
        print("Please learn these concepts properly")

    return  new_sub_welcome_method()
new_welcome(len,[1,2,3,4,5])
"""


"""

# decorator
def new_welcome(func):
    def new_sub_welcome_method():
        print("Welcome to the advanced python course")
        func()
        print("Please learn these concepts properly")

    return  new_sub_welcome_method()

@new_welcome
def course_introduction():
    print("This is an advanced python course")

"""

# more decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")

    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*arg, **kwargs):
            for _ in range(n):
                func(*arg, **kwargs )
        return wrapper
    return decorator

@repeat(3)
def say_bye():
    print("Bye Bye!")

say_bye()