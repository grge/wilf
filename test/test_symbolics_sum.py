from numbers import Number
from wilf.symbolics import SymbolicExpression, Expression, Sum, Symbol

def test_sum_type_is_expression():
    s = Sum(1, 2)
    assert isinstance(s, Expression)

def test_sum_type_is_symbolic_expression():
    s = Sum(1, 2)
    assert isinstance(s, SymbolicExpression)

def test_sums_can_be_compared():
    s1 = Sum(1, 2)
    s2 = Sum(1, 2)
    s3 = Sum(1, 3)
    assert s1 == s2
    assert s1 != s3

def test_sum_str_two_numbers():
    s = Sum(1, 2)
    assert str(s) == '1 + 2'

def test_sum_str_four_numbers():
    s = Sum(1, 2, 3, 4)
    assert str(s) == '1 + 2 + 3 + 4'

def test_sum_terms_are_stored():
    s = Sum(1, 2)
    assert s.terms == (1, 2)

def test_sum_one_argument_simplified_is_just_the_value():
    s = Sum(1).simplify()
    assert s == 1

def test_sum_simplifies_to_number():
    s = Sum(1, 2).simplify()
    assert isinstance(s, Number)
    assert s == 3

def test_sum_can_construct_with_many_terms():
    s = Sum(1, 2, 3, 4)
    assert s.terms == (1, 2, 3, 4)

def test_sum_with_many_numbers_simplifies_to_sum():
    s = Sum(1, 2, 3, 4).simplify()
    assert isinstance(s, Number)
    assert s == 10

def test_sum_of_sums_of_numbers_simplifies_to_sum():
    s = Sum(Sum(1, 2), Sum(3, 4)).simplify()
    assert s == 10

def test_sum_of_sums_initialises_flat():
    s = Sum(Sum(1, 2), 3)
    assert s == Sum(1, 2, 3)

    s = Sum(Sum(1, 2), Sum(3, 4))
    assert s == Sum(1, 2, 3, 4)

def test_sum_of_numeric_and_symbol():
    x = Symbol('x')
    s = Sum(1, x)
    assert s.terms == (1, x)

def test_sum_with_symbol_cannot_simplify():
    x = Symbol('x')
    s = Sum(1, x).simplify()
    assert s.terms == (1, x)

def test_simplified_sum_has_summed_numbers_first():
    x = Symbol('x')
    s = Sum(x, 1).simplify()
    assert s.terms == (1, x)

def test_sum_with_symbol_simplifies_numeric_terms():
    x = Symbol('x')
    s = Sum(1, x, 1, 1).simplify()
    assert s.terms == (3, x)

def test_sum_of_sums_with_symbols_simplifies_to_flat():
    x = Symbol('x')
    y = Symbol('y')
    s = Sum(Sum(1, x), Sum(1, y)).simplify()
    assert s.terms == (2, x, y)


