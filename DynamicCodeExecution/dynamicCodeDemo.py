def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""

    # execute the code string
    # exec = executes the given source in the context of globals and locals
    # global scope = entire python file
    # local scope = where it is executed

    local_scope = {}
    exec(code, {}, local_scope)
    print(local_scope["greet"]("Alice"))

def demonstrate_eval():
    # evaluate the expression
    expression = input("Enter expression: ")
    result = eval(expression) # danger - can access other pieces of code/ ill modification

    print(f"Result of eval: {result}\n")


def demonstrate_safe_eval():
    expression = input("Enter expression that uses a, b and c: ")

    # define variables for the expression
    variables = {"a": 2, "b": 3, "c": 4}

    # evaluate the expression in the context of the provided variables
    result = eval(expression, {}, variables)

    print(f"Result of eval: {result}\n")

demonstrate_safe_eval()