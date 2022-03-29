from functools import reduce

def product(it):
    return reduce(lambda x, y: x * y, it, 1)

def factorial(n):
    return product(range(1, n + 1))