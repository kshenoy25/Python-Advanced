# variable annotations

name: str = "Alice"
age: int = 30

is_student: bool = False



def greet(person: str, age: int) -> str:
    # creating a doc string = defining what the function actually does giving some documentation for it
    # python can automatically pick that up and use it in a meaningful way
    """

    Greets a person by name and age.

    :param person:  The name of the person (expected tp be a string).
    :param age: The age of the person (expected to be an integer).
    :return: A greeting message (expected tp be a string).
    """

    return f"Hello, {person}! You are {age} years old."

# function annotations

# using the function
greeting_message = greet(name, age)
print(greeting_message)


# showing the annotations
print("\nFunction Annotations:", greet.__annotations__)
#print("Variable Annotations:", __annotations__)