from wilf.symbolics import Sum, Product, Symbol, Power, Fraction

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

def test_x_plus_1():
    assert x + 1 == Sum(1, x)

def test_x_times_2():
    assert x * 2 == Product(2, x)

def test_x_to_the_3():
    assert x ** 3 == Power(x, 3)

def test_x_to_the_y():
    assert x ** y == Power(x, y)

def test_fraction():
    assert 1 / x == Fraction(1, x)

def test_long_sum():
    assert x + 1 + y == Sum(1, x, y)

def test_nested_sum():
    assert x + 2 + (y + 5) == Sum(7, x, y)

def test_sum_of_products():
    assert (x + 2) * (y + 3) == Product(Sum(2, x), Sum(3, y))

def test_sum_times_products():
    assert (x + 2) * (y * 3) == Product(3, Sum(2, x), y)

def test_x_minus_1():
    assert x - 1 == Sum(-1, x)

def test_x_times_negative_1():
    assert x * -1 == Product(-1, x)

def test_product_collect_negative_1():
    assert x * y * -z == Product(-1, x, y, z)

def test_1_over_2():
    assert x / 2 == Fraction(x, 2)
