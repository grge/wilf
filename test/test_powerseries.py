from pytest import approx
from wilf.powerseries import PowerSeries, exp, derivative, integral
from wilf.utils import factorial

x = PowerSeries.x

def equal_upto_o(a, b, o=10):
    return all(a.f(order) == b.f(order) for order in range(o))

def test_powerseries_add():
    a = x + 1
    b = 2*x
    c = a + b
    assert equal_upto_o(c, 3 * x + 1)

def test_powerseries_mul():
    a = x + 1
    b = 2*x
    c = a * b
    assert equal_upto_o(c, 2*x**2 + 2*x)

def test_powerseries_derivative():
    a = 13*x**2 + 23*x + 1
    d = derivative(a)
    assert equal_upto_o(derivative(a), 26*x + 23)

def test_integral_derivative():
    a = 3*x**2 + 2*x + 1
    # note: need to add back the constant term after integration
    assert equal_upto_o(1 + integral(derivative(a)), a)

def test_geometric_series():
    gs = 1 / (1 - x)
    for coef_ix in range(20):
        assert gs.f(coef_ix) == 1

def test_exp():
    e_to_x = exp(x)
    for coef_ix in range(20):
        assert e_to_x.f(coef_ix) == approx(1 / factorial(coef_ix))
        