from wilf.symbolics import SymbolicExpression, Expression, Power, Symbol

def test_power_is_expression():
    p = Power(2, 3)
    assert isinstance(p, Expression)

def test_power_is_symbolic_expression():
    p = Power(2, 3)
    assert isinstance(p, SymbolicExpression)

def test_power_can_be_compared():
    p1 = Power(2, 3)
    p2 = Power(2, 3)
    p3 = Power(2, 4)
    assert p1 == p2
    assert p1 != p3

def test_power_str():
    p = Power(2, 3)
    assert str(p) == '2^3'

def test_base_and_exponent_attributes():
    p = Power(2, 3)
    assert p.base == 2
    assert p.exponent == 3

def test_simplify_computes_power():
    p = Power(2, 3).simplify()
    assert p == 8

def test_simplify_with_symbol_exponent():
    p = Power(2, Symbol('x')).simplify()
    assert p.base == 2
    assert p.exponent == Symbol('x')

def test_simplify_with_symbol_base():
    p = Power(Symbol('x'), 2).simplify()
    assert p.base == Symbol('x')
    assert p.exponent == 2

def test_simplify_with_zero_exponent():
    p = Power(2, 0).simplify()
    assert p == 1
    p = Power(Symbol('x'), 0).simplify()
    assert p == 1

def test_simplify_with_zero_base():
    p = Power(0, 2).simplify()
    assert p == 0
    p = Power(0, Symbol('x')).simplify()
    assert p == 0

def test_simplify_with_one_exponent():
    p = Power(2, 1).simplify()
    assert p == 2
    p = Power(Symbol('x'), 1).simplify()
    assert p == Symbol('x')

def test_simplify_with_one_base():
    p = Power(1, 1).simplify()
    assert p == 1
    p = Power(1, Symbol('x')).simplify()
    assert p == 1

def test_simplify_no_numeric():
    p = Power(Symbol('x'), Symbol('y')).simplify()
    assert p.base == Symbol('x')
    assert p.exponent == Symbol('y')