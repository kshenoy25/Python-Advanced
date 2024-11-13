def topten():


    """
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    """
    n = 1
    while n <= 10:
        sq = n**2
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)