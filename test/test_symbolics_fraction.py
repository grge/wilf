from wilf.symbolics import SymbolicExpression, Expression, Fraction, Symbol

def test_fraction_is_expression():
    f = Fraction(2, 3)
    assert isinstance(f, Expression)

def test_fraction_is_symbolic_expression():
    f = Fraction(2, 3)
    assert isinstance(f, SymbolicExpression)

def test_fraction_str():
    f = Fraction(2, 3)
    assert str(f) == '2/3'

def test_fractions_can_be_compared():
    f1 = Fraction(2, 3)
    f2 = Fraction(2, 3)
    f3 = Fraction(2, 4)
    assert f1 == f2
    assert f1 != f3

def test_fraction_numerator_denominator_attributes():
    f = Fraction(2, 3)
    assert f.numerator == 2
    assert f.denominator == 3

def test_fraction_simplify_computes_fraction():
    f = Fraction(2, 4).simplify()
    assert f == 1/2

def test_fraction_simplify_with_symbol():
    p = Fraction(Symbol('x'), 2).simplify()
    assert p.numerator == Symbol('x')
    assert p.denominator == 2

def test_fraction_simplify_with_zero_numerator():
    p = Fraction(0, 2).simplify()
    assert p == 0
    p = Fraction(0, Symbol('x')).simplify()
    assert p == 0

def test_fraction_simplify_with_zero_denominator():
    p = Fraction(2, 0).simplify()
    assert p == float('inf')
    p = Fraction(Symbol('x'), 0).simplify()
    assert p == float('inf')

def test_fraction_simplify_with_one_denominator():
    p = Fraction(2, 1).simplify()
    assert p == 2
    p = Fraction(Symbol('x'), 1).simplify()
    assert p == Symbol('x')