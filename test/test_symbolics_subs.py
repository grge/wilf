from wilf.symbolics import Sum, Product, Fraction, Power, Symbol


def test_symbol():
    x = Symbol('x')
    assert x.name == 'x'

def test_symbol_to_str():
    x = Symbol('x')
    assert str(x) == 'x'

def test_symbol_identity():
    x1 = Symbol('x')
    x2 = Symbol('x')
    y = Symbol('y')
    assert x1 == x2
    assert x1 != y

def test_subs_symbol_for_value():
    x = Symbol('x')
    assert x.subs({x: 2}) == 2

def test_subs_symbol_for_other_symbol():
    x = Symbol('x')
    y = Symbol('y')
    assert x.subs({x: y}) == y

def test_subs_symbol_for_complex_expression():
    x = Symbol('x')
    expr = Sum(1, Product(5, x))
    assert x.subs({x: expr}) == expr

def test_subs_symbol_simplify_option():
    x = Symbol('x')
    expr = Sum(1, Product(x, 5), 4)
    assert x.subs({x: expr}, simplify=True) == Sum(5, Product(5, x))
    assert x.subs({x: expr}, simplify=False) == Sum(1, Product(x, 5), 4)

def test_subs_sum():
    x = Symbol('x')
    expr = Sum(x, 10)
    assert expr.subs({x: 1}) == 11

def test_subs_product():
    x = Symbol('x')
    expr = Product(x, 10)
    assert expr.subs({x: 20}) == 200

def test_subs_fraction():
    x = Symbol('x')
    expr = Power(x, 10)
    assert expr.subs({x: 2}) == 1024

def test_subs_fraction_no_simplify():
    x = Symbol('x')
    expr = Power(x, 10)
    assert expr.subs({x: 2}, simplify=False) == Power(2, 10)


