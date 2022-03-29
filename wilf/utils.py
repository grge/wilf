from functools import reduce

def product(it):
    return reduce(lambda x, y: x * y, it, 1)