# errors and exceptions

# syntax error example
# = 5 print(a)

# type error
#b = 6 + "s"

# MORE ERRORS

# module not found error
# name error
# file not found error
# value error --> right type - inappropriate value
# index error

# raising an exception
"""

x = -5
if x < 0:
    raise Exception("Negative value is not allowed")

"""


# assert statement
#y = -8
#assert(y >= 0), "y is not positive"

"""
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print("Division by zero is not allowed")
except TypeError as e:
    print("Type error is not allowed")
else:
    print("Everything seems to be in working order!")
finally:
    print("Just cleaning up...")

"""

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value too high")
    if x < 5:
        raise ValueTooLowError("Value too low:", x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)