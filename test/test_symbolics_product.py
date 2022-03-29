from numbers import Number
from wilf.symbolics import SymbolicExpression, Expression, Product, Symbol

def test_product_type_is_expression():
    p = Product(1, 2)
    assert isinstance(p, Expression)

def test_product_type_is_symbolic_expression():
    p = Product(1, 2)
    assert isinstance(p, SymbolicExpression)

def test_products_can_be_compared():
    p1 = Product(1, 2)
    p2 = Product(1, 2)
    p3 = Product(1, 3)
    assert p1 == p2
    assert p1 != p3

def test_product_str_two_numbers():
    p = Product(1, 2)
    assert str(p) == '1 * 2'

def test_sum_str_four_numbers():
    p = Product(1, 2, 3, 4)
    assert str(p) == '1 * 2 * 3 * 4'

def test_product_terms_are_stored():
    p = Product(1, 2)
    assert p.terms == (1, 2)

def test_product_one_argument_simplified_is_just_the_value():
    p = Product(1).simplify()
    assert p == 1

def test_product_simplifies_to_number():
    p = Product(2, 3).simplify()
    assert isinstance(p, Number)
    assert p == 6

def test_product_can_construct_with_many_terms():
    p = Product(1, 2, 3, 4)
    assert p.terms == (1, 2, 3, 4)

def test_product_with_many_numbers_simplifies_to_value():
    p = Product(2, 3, 4).simplify()
    assert isinstance(p, Number)
    assert p == 24

def test_product_of_products_of_numbers_simplifies_to_value():
    p = Product(Product(2, 3), Product(4, 5)).simplify()
    assert p == 120

def test_product_of_products_initialises_flat():
    p = Product(Product(1, 2), 3)
    assert p == Product(1, 2, 3)

    p = Product(Product(1, 2), Product(3, 4))
    assert p == Product(1, 2, 3, 4)

def test_product_of_numeric_and_symbol():
    x = Symbol('x')
    p = Product(2, x)
    assert p.terms == (2, x)

def test_product_of_one_with_symbol_returns_the_symbol():
    x = Symbol('x')
    p = Product(1, x).simplify()
    assert p == x

def test_product_of_one_and_symbols_returns_the_product_of_symbols():
    x = Symbol('x')
    y = Symbol('y')
    p = Product(1, x, y).simplify()
    assert p == Product(x, y)

def test_product_containing_zero_is_zero():
    x = Symbol('x')
    p = Product(1, x, 10, 0).simplify()
    assert p == 0

def test_simplified_product_has_numbers_first():
    x = Symbol('x')
    p = Product(x, 2).simplify()
    assert p.terms == (2, x)

def test_sum_with_symbol_simplifies_numeric_terms():
    x = Symbol('x')
    p = Product(1, x, 1, 2).simplify()
    assert p.terms == (2, x)

def test_sum_of_sums_with_symbols_simplifies_to_flat():
    x = Symbol('x')
    y = Symbol('y')
    s = Product(Product(3, x), Product(2, y)).simplify()
    assert s.terms == (6, x, y)
