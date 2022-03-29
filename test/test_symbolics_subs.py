from wilf.symbolics import Sum, Product, Fraction, Power, Symbol

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

def test_symbol():
    assert x.name == 'x'

def test_symbol_to_str():
    assert str(x) == 'x'

def test_symbol_identity():
    x1 = Symbol('x')
    x2 = Symbol('x')
    y = Symbol('y')
    assert x1 == x2
    assert x1 != y

def test_subs_symbol_for_value():
    assert x.subs({x: 2}) == 2

def test_subs_symbol_for_other_symbol():
    assert x.subs({x: y}) == y

def test_subs_symbol_for_complex_expression():
    expr = Sum(1, Product(5, x))
    assert x.subs({x: expr}) == expr

def test_subs_symbol_simplify_option():
    expr = Sum(1, Product(x, 5), 4)
    assert x.subs({x: expr}, simplify=True) == Sum(5, Product(5, x))
    assert x.subs({x: expr}, simplify=False) == Sum(1, Product(x, 5), 4)

def test_subs_sum():
    expr = Sum(x, 10)
    assert expr.subs({x: 1}) == 11

def test_subs_product():
    expr = Product(x, 10)
    assert expr.subs({x: 20}) == 200

def test_subs_fraction():
    expr = Power(x, 10)
    assert expr.subs({x: 2}) == 1024

def test_subs_fraction_no_simplify():
    expr = Power(x, 10)
    assert expr.subs({x: 2}, simplify=False) == Power(2, 10)

def test_subs_symbol_with_other():
    expr = Fraction(1, x) + x
    assert expr.subs({x: y}) == Fraction(1, y) + y

def test_subs_sub():
    expr = Sum(Power(Sum(x, y), 2), 1)
    assert expr.subs({Sum(x, y): x}) == Sum(1, Power(x, 2))
    # This is the same test, but using the dunder methods
    expr = (x + y)**2 + 1
    assert expr.subs({(x + y): z}) == z**2 + 1
