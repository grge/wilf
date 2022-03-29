from pytest import approx
from wilf.powerseries import PowerSeries, exp
from wilf.utils import factorial
from wilf.symbolics import Symbol

t = Symbol('t')
x = PowerSeries.x
        
def test_mul_symbol():
    a = t * x
    assert isinstance(a, PowerSeries)
    assert [a.f(i) for i in range(5)] == [0, t, 0, 0, 0]

def test_rmul_symbol():
    a = x * t
    assert isinstance(a, PowerSeries)
    assert [a.f(i) for i in range(5)] == [0, t, 0, 0, 0]

def test_add_symbol():
    a = x + t
    assert isinstance(a, PowerSeries)
    assert [a.f(i) for i in range(5)] == [t, 1, 0, 0, 0]

def test_geometric_series():
    a = 1/(1 - t*x) 
    assert isinstance(a, PowerSeries)
    assert [a.f(i) for i in range(5)] == [1, t, t*t, t*t*t, t*t*t*t]

def test_legendre():
    legendre = 1/((1 - 2 * x * t + x**2)**0.5)
    assert legendre.f(0) == 1
    assert legendre.f(1) == t
    assert legendre.f(2).subs({t: 0}) == -1/2
    assert legendre.f(2).subs({t: 1}) == 1
    assert legendre.f(2).subs({t: -1}) == 1